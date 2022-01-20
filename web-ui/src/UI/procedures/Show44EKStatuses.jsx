import React, { useState,  useEffect } from 'react';
import procedureService from '../../API/procedureService';

import ShowStatuses from '../ShowStatuses';
const Show44EKStatuses = () => {
    
    const [statuses, setStatuses] = useState([])    
    
    useEffect(() => {
        const res = procedureService.get44EKStatuses()
        res.then(res => setStatuses(res))
    }, [])
    return (
        <div>
            <ShowStatuses EA={false} statuses={statuses}/>
        </div>
    );
};

export default Show44EKStatuses;