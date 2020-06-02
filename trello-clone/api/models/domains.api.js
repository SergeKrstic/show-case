class DomainApi {
  constructor(baseApi, collectionRef) {
    this._baseApi = baseApi;
    this._collectionRef = collectionRef;
  }

  // read operations
  // ==========================================================================

  get = async id => {
    return this._baseApi.get(this._collectionRef, id);
  };

  getAll = async () => {
    return this._baseApi.getAll(this._collectionRef);
  };

  // write operations
  // ==========================================================================

  add = async data => {
    return this._baseApi.add(this._collectionRef, data);
  };

  // write operations, batch processing supported
  // ==========================================================================

  set = async (id, data, batch = null) => {
    return this._baseApi.set(this._collectionRef, id, data, batch);
  };

  update = async (id, data, batch = null) => {
    return this._baseApi.update(this._collectionRef, id, data, batch);
  };

  delete = async (id, batch = null) => {
    return this._baseApi.delete(this._collectionRef, id, batch);
  };
}

export default DomainApi;
