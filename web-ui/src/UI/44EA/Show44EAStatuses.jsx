import React ,{useEffect,useState}from 'react';
import procedureService from '../../API/procedureService';

import ShowStatuses from '../ShowStatuses';

const Show44EAStatuses = () => {
    const [statuses, setStatuses] = useState([])    
    
    useEffect(() => {
        const res = procedureService.get44EAStatuses()
        res.then(res => console.log(res))
        res.then(res => setStatuses(res))
    }, [])
    return (
        <div>
            <ShowStatuses EA={true} statuses={statuses} />
        </div>
    );
};

export default Show44EAStatuses;