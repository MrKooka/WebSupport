import axios from "axios"

class procedureService {

    static async get44ekStatuses() {
        const res = await axios.get('http://127.0.0.1:8000/api/44ek/getProcedureStatus')
        return res.data
    }
    static async get44ekProcedureInfo(regNum) {
        const res = await axios.get(`http://127.0.0.1:8000/api/44ek/?regNum=${regNum}`)
        return res.data
    }

    
    static async get44EAStatuses() {
        const res = await axios.get(`http://127.0.0.1:8000/api/44ea/get44EAProcedureStatus`)
        return res.data
    }
    static async get44EKStatuses() {
        const res = await axios.get(`http://127.0.0.1:8000/api/44ek/getProcedureStatus`)
        console.log('get to /api/44ek/getProcedureStatus');
        return res.data
    }
    static async loadProtocols(regNum) {
        const res = await axios.get(`http://127.0.0.1:8000/api/protocol/getprotocol?regNum=${regNum}`)
        console.log('get to /api/protocol/getprotocol');
        return res.data
    }
}



export default procedureService