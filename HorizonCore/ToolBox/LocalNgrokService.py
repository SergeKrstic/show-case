# Note: Need to start Django's ORM before importing models
import HorizonBackend.core.runtime  # <-- REQUIRED, DO NOT DELETE !!

import subprocess
import requests
import json
import time
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from HorizonBackend.trello_webhooks.models import Webhook


class Auth:
    MessengerLogin = config('MESSENGER_LOGIN')
    MessengerPassword = config('MESSENGER_PASSWORD')
    MessengerVerifyToken = config('MESSENGER_VERIFY_TOKEN')

    DialogFlowLogin = config('DIALOG_FLOW_LOGIN')
    DialogFlowPassword = config('DIALOG_FLOW_PASSWORD')

    TrelloToken = config('TRELLO_RESOURCE_OWNER_TOKEN')


def openBrowser():
    _browser = webdriver.Chrome(executable_path='/Applications/chromedriver')
    _browser.implicitly_wait(3)
    return _browser


# Local ngrok dashboard --> http://127.0.0.1:4040/status

# Overview:
#   1. Run 'LocalDjangoWebServer' configuration
#   2. Run 'LocalNgrokService' configuration -- (which runs this Python file)
#   3. Run 'LocalVessel' configuration

if __name__ == '__main__':

    # 1. Start the Horizon web app (LocalHorizonWebServer.py)
    # --> This needs to be started manually

    # 2. Start ngrok
    print('')
    try:
        requests.get("http://localhost:4040/api/tunnels")
        print('Ngrok server already running!')
    except:
        print('Starting ngrok server...')
        subprocess.Popen('~/ngrok http 8000', stdout=subprocess.PIPE, shell=True)
        time.sleep(5)

    # 3. Obtain forwarding address
    print('Retrieving ngrok public url...')
    response = requests.get("http://localhost:4040/api/tunnels")
    ngrokData = json.loads(response.text)

    publicUrl = ''
    for tunnel in ngrokData['tunnels']:
        if tunnel['proto'] == 'https':
            publicUrl = tunnel['public_url']

    if publicUrl == '':
        print('Failed to retrieve ngrok public url')
        print('Exiting...')
    else:

        # 4. Configure DialogFlow webhook address using Selenium with ngrok forwarding address
        print('Configuring DialogFlow webhooks...')
        browser = openBrowser()
        browser.get('https://console.dialogflow.com/api-client/#/login')
        browser.find_element_by_class_name('md-btn-login-text-wrapper').click()
        browser.find_element_by_name('identifier').send_keys(Auth.DialogFlowLogin, Keys.ENTER)
        browser.find_element_by_name('password').send_keys(Auth.DialogFlowPassword, Keys.ENTER)
        time.sleep(10)
        browser.get('https://console.dialogflow.com/api-client/#/agent/5fd539bd-57ef-48e2-92ba-cf75f64a33fb/fulfillment')
        time.sleep(10)
        browser.find_element_by_name('webhookUrl').clear()
        browser.find_element_by_name('webhookUrl').send_keys(publicUrl + '/chatbot/webhook-for-dialogflow')
        buttons = browser.find_elements_by_tag_name('button')
        for button in buttons:
            if button.text == "SAVE":
                button.click()
                break

        # 5. Configure Messenger webhook address using Selenium with ngrok forwarding address
        print('Configuring Messenger webhooks...')
        browser.get('https://developers.facebook.com/apps/')
        browser.find_element_by_id('email').send_keys(Auth.MessengerLogin)
        browser.find_element_by_id('pass').send_keys(Auth.MessengerPassword, Keys.ENTER)
        browser.get('https://developers.facebook.com/apps/168911567069861/webhooks/')
        browser.find_element_by_link_text('Edit Subscription').click()
        browser.find_element_by_name('callback_url').clear()
        browser.find_element_by_name('callback_url').send_keys(publicUrl + '/chatbot/webhook-for-facebook-messenger')
        browser.find_element_by_name('verify_token').send_keys(Auth.MessengerVerifyToken, Keys.ENTER)
        browser.close()

        # 6. Configure Trello webhooks with ngrok forwarding address
        print('Configuring Trello webhooks...')

        trelloModels = [
            {"trello_model_id": "59797961fce7f8de830ddc78", "description": "Personal >> ..Today"},
            {"trello_model_id": "57806ba77140b4a3a345716d", "description": "Personal >> .Dashboard"},
            {"trello_model_id": "5b03cdc6a2fb0e609270386c", "description": "Personal >> Locations"},
            {"trello_model_id": "5af942fb687082db1fb4eece", "description": "Projects >> Local Test Board"},
            {"trello_model_id": "5b03cac026a57f0804551d78", "description": "References >> Consumables - Household"},
            {"trello_model_id": "5b03ca9197d5df2284d6d119", "description": "References >> Consumables - Fridge"},
            {"trello_model_id": "5b03cae4840b167742940225", "description": "References >> Consumables - Pantry"},
        ]

        for trelloModel in trelloModels:
            try:
                localWebhook = Webhook.objects.get(trello_model_id=trelloModel["trello_model_id"])
            except:
                print('creating webhook...')
                localWebhook = Webhook.objects.create(
                    trello_model_id=trelloModel["trello_model_id"],
                    description=trelloModel["description"],
                    auth_token=Auth.TrelloToken,
                )

            localWebhook.save()

        # 7. Run forever...
        print('\nRunning local ngrok service...')
        while True:
            # Note: ngrok will run forever even without this
            # loop. However, by using this loop, you are forced
            # to terminate this script, which will also
            # terminate ngrok.
            time.sleep(1)

    # 8. Start the Vessel (Horizon background services - Vessel.py)
    # --> This needs to be started manually
