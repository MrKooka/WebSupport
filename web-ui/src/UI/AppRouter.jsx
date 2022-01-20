import React from 'react';
import {
    Routes,
    Route,
    Navigate
} from "react-router-dom";
import Show44EAStatuses from './44EA/Show44EAStatuses';
import Show44EKStatuses from './procedures/Show44EKStatuses';
import CancelProtocolForm from './procedures/CancelProtocolForm';


import ShowStatuses from './ShowStatuses';
import UpdateFrorm from './UpdateFrorm';
import MergeUser from './elk/MergeUser';
import ShowArticles from './articles/ShowArticles';
import ErDiag from './erDiagram/ErDiag';

const AppRouter = () => {
    return (
        <Routes>
        
            <Route path='44ek/updateForm' element={<UpdateFrorm/>}/>
            <Route path='44ea/statuses' element={<Show44EAStatuses/>}/>
            <Route path='44ek/statuses' element={<Show44EKStatuses/>}/>
            <Route path='44ek/cancelprotocol' element={<CancelProtocolForm/>}/>
            <Route path='elk/mergeusers' element={<MergeUser/>}/>
            <Route path='articles' element={<ShowArticles/>}/>
            <Route path='erdiag' element={<ErDiag/>}/>
            
            
            

            
            

            
            

            

        </Routes>
    );
};

export default AppRouter;