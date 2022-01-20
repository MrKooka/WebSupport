import axios from "axios";

const updateForm = {
    procedure: {
      status: [],
      requestEndDateTime: '',
      requestReviewFirstPartsDateTime: '',
      offerDate: '',
      offerEndDateTime: '',
      requestReviewSecondPartsDateTime: '',
      id: ''
    },
    lot: {
      status: [],
      id: ''
    },
    protocol: {
      deleted_at: new Date(Date.now()).toISOString().slice(0, 19).replace('T', ' ').replace('Z', ''),
      active: '',
      archive: '',
      id: ''
    },
    request: {
      status: '',
      id: ''
    },
    procedureEvent: {}

  }

// const updateForm = {...updateForm.procedure, requestEndDateTime:'123'}
// console.log({...updateForm,procedure:{...updateForm.procedure, requestEndDateTime:'123'} });
// console.log(updateForm);
const res = axios.get(axios.get(`http://127.0.0.1:8000/api/44ek/?regNum=0318100071821000103`).then(res =>console.log(res.data.lot[0].id)))
const updateForm  = {...updateForm , procedureEvent:{id:res.lot.protocol}}
console.log(updateForm);