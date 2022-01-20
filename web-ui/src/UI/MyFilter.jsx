import React from 'react';
import { Table, Col, Button, Form, Row, ButtonGroup } from 'react-bootstrap'

const MyFilter = props => {
    function onlyUnique(value, index, self) {
        return self.indexOf(value) === index;
    }
    // props.EA = false
    const statusesType = props.statuses.map(s => s.type)
    const unique = statusesType.filter(onlyUnique);
    const eaOrNot = () => {
        if (props.EA) {
            const lotStatusesDesc = {
                procedurestatus: 'Процедуры',
                lotstatus: 'Лот',
                contractstatus: 'Контракт',
                requeststatus: 'Заявка',
                protocolstatus: 'Протокол',
                explanationstatus: 'Разъяснение',
                informationrequeststatus: 'informationrequeststatus',
                requestcustomerstatus: 'requestcustomerstatus',
                contractrefusestatus: 'contractrefusestatus',
                uploadformtaskstatus: 'uploadformtaskstatus'

            }
            return lotStatusesDesc
        } else {

            const lotStatusesDesc = {
                'etp.repository.catalog.procedure.status.procedure': 'Процедура',
                'etp.repository.catalog.procedure.status.lot':'Лот',
                'etp.repository.catalog.procedure.status.request':'Заявка',
                'etp.repository.catalog.procedure.status.request.additional':'request.additional'
            }
            return lotStatusesDesc


        }
    }


    return (
        <div>
            <Form.Label>Фильтр статусов</Form.Label>
            <Form.Select size="sm" onChange={e => props.setFilter({ ...props.filter, sort: e.target.value })}>
                {props.EA
                    ?
                    unique.map(item => <option key={item} value={item}>{eaOrNot()[item]}</option>)
                    :
                    unique.map(item => <option key={item} value={item}>{eaOrNot()[item]}</option>)
                }
                {/* // {unique.map(item => <option key={item} value={item}>{lotStatusesDesc[item]}</option>)} */}
            </Form.Select>
        </div>
    );
};

export default MyFilter;