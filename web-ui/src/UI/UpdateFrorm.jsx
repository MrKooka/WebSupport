import React, { useState, useEffect } from 'react';
import { Form, Button, FormControl, Row, Col } from 'react-bootstrap';
import { DateTimePickerComponent } from '@syncfusion/ej2-react-calendars';
import CodeHighlArea from './CodeHighlArea';
import procedureService from '../API/procedureService'
const UpdateFrorm = (props) => {
    const [statuses, setStatuses] = useState([])
    const [regNumInpt, setRegNumInpt] = useState('')
    const [procInfo, setProcInfo] = useState({})
    const [updateForm, setUpdateForm] = useState({
        procedure: {
            status: [],
            requestEndDateTime: '',
            requestReviewFirstPartsDateTime: '',
            offerDate: '',
            offerEndDateTime: '',
            requestReviewSecondPartsDateTime: '',
            id: ''
        },
        lot: {},
        protocol: {},
        request: {
            status: '',
            id: ''
        },
        procedureEvent: {
            protocolId: '',
            id: []
        }

    })

    useEffect(() => {
        const offerEndDateTime = CreateDate('', true)
        console.log('log offerEndDateTime', offerEndDateTime);
        setUpdateForm({ ...updateForm, procedure: { ...updateForm.procedure, offerEndDateTime: offerEndDateTime } })
        console.log('Сработала useEffect  для offerEndDateTime');
    }, [updateForm.procedure.offerDate])

    useEffect(() => {
        let res = procedureService.get44ekStatuses()
        res.then(res => setStatuses(res))
        console.log(procInfo);
    }, [])

    useEffect(() => {
        try {
            if (Object.keys(procInfo).length > 0) {
                setUpdateForm({
                    ...updateForm,
                    procedure: { ...updateForm.procedure, id: procInfo && procInfo.id },
                    lot: { id: procInfo.lot && procInfo.lot.id },
                    protocol: { id: procInfo.lot && procInfo.lot.protocol.map(p => p.id), deleted_at: new Date(Date.now()).toISOString().slice(0, 19).replace('T', ' ').replace('Z', '') },
                    request: { ...procInfo.lot.request, id: procInfo.lot && procInfo.lot.request.map(req => req.id) },
                    procedureEvent: { ...updateForm.procedureEvent, id: getIdForProtocolEvents() }
                })
            }

        }catch(e){
            console.log(procInfo);
            console.log(e);
        }
        

    }, [procInfo])
    const CreateDate = (props, offerEndDateTime = false) => {
        const tzoffset = (new Date()).getTimezoneOffset() * 60000; //offset in milliseconds

        if (offerEndDateTime && updateForm.procedure.offerDate) {
            let oldDate = Date.parse(updateForm.procedure.offerDate) - tzoffset
            const newDate = new Date(oldDate + 10800000).toISOString().slice(0, 19).replace('T', ' ').replace('Z', '')
            return newDate
        }
        if (props.value) {

            let oldDate = Date.parse(props.value) - tzoffset
            const newDate = new Date(oldDate).toISOString().slice(0, 19).replace('T', ' ').replace('Z', '')
            return newDate
        }
    }

    const getProcedureInfo = () => {
        let res = procedureService.get44ekProcedureInfo(regNumInpt)
        res.then(res => setProcInfo(res))
        console.log(`http://127.0.0.1:8000/api/44ek/?regNum=${regNumInpt}`);
    }

    const getIdForProtocolEvents = () => {
        let eventIdArray = []
        if (procInfo.lot) {
            let events = procInfo.lot.protocol.map(p => p.event)

            events.forEach(event => {
                // console.log(event);
                if (event[0]) {
                    eventIdArray.push(...event.map(e => e.id))
                }

            });
        }
        return eventIdArray
    }
    const sql = `
  UPDATE procedures SET
  status = '${updateForm.procedure.status}', -- Статус процедуры
  requestEndDateTime = '${updateForm.procedure.requestEndDateTime}', -- Дата и время окончания срока подачи заявок
  requestReviewFirstPartsDateTime = '${updateForm.procedure.requestReviewFirstPartsDateTime}', -- Дата и время рассмотрения и оценки первых частей заявок
  offerDate = '${updateForm.procedure.offerDate}', -- Дата подачи окончательных предложений
  offerEndDateTime = '${updateForm.procedure.offerEndDateTime}',  --Дата подачи окончательных предложений +3 часа (всегда так, в задаче не указывают)
  requestReviewSecondPartsDateTime = '${updateForm.procedure.requestReviewSecondPartsDateTime}' -- Дата и время рассмотрения и оценки вторых частей заявок
  WHERE id = ${updateForm.procedure.id};

  UPDATE lot SET
  status = '${updateForm.lot.status}' WHERE id = ${updateForm.lot.id}; -- Статус лота, такой же как и у процедуры, только lot.
  
  UPDATE protocol SET deleted_at = '${updateForm.protocol.deleted_at}', active = 0, archive = 1 WHERE id IN (${updateForm.protocol.id}); -- Протоколы которые требуется отменить.

  UPDATE request set
  status = 'request.published' WHERE id IN (${updateForm.request.id}); -- Статус заявок, published - подана \ returned - возвращена. В случае возвращена active=0|archive=1

 UPDATE procedureEvent SET procedureId = NULL, lotId = NULL, protocolId = NULL WHERE id IN  (${updateForm.procedureEvent.id}); -- На приеме заявок убираем все события
  `
    return (

        <div>
            <Row className={['d-flex', 'justify-content-start', 'mt-2'].join(' ')}>
                <Col className={['col-5'].join(' ')}>
                    <FormControl value={regNumInpt} onChange={(e) => setRegNumInpt(e.target.value)} />
                </Col>
                <Col>
                    <Button variant="contained" onClick={getProcedureInfo}>Загрузить</Button>
                </Col>
            </Row>
            <Row className={['col-3'].join(" ")} style={{ paddingLeft: "15px" }}>

                <Form onSubmit={(e) => {
                    e.preventDefault()
                    console.log(e.target)
                }}>
                    <div class="mb-3">
                        <label class="form-label">Статус процедуры</label>
                        <Form.Select size="lg" value={updateForm.status} onChange={(e) => setUpdateForm({ ...updateForm, procedure: { ...updateForm.procedure, status: e.target.value } })}>
                            {statuses.map((s) => <option value={s.code} >{s.name}</option>)}
                        </Form.Select>
                    </div>

                    <div class="mb-3">
                        <label class="form-label">Дата и время окончания срока подачи заявок</label>
                        <DateTimePickerComponent
                            change={(props) => {
                                const newDate = CreateDate(props)
                                setUpdateForm({ ...updateForm, procedure: { ...updateForm.procedure, requestEndDateTime: newDate } })
                            }}
                            value={updateForm.procedure.requestEndDateTime}
                            format="yyy-MM-dd- HH:mm:ss"
                            step={60}
                        >
                        </DateTimePickerComponent>
                    </div>
                    <div class="mb-3">
                        <label class="form-label"> Дата и время рассмотрения и оценки первых частей заявок</label>
                        <DateTimePickerComponent
                            change={(props) => {
                                const newDate = CreateDate(props)
                                setUpdateForm({ ...updateForm, procedure: { ...updateForm.procedure, requestReviewFirstPartsDateTime: newDate } })
                            }}
                            value={updateForm.procedure.requestReviewFirstPartsDateTime}
                            format="yyy-MM-dd- HH:mm:ss"
                            step={60}
                        >
                        </DateTimePickerComponent>
                    </div>

                    <div class="mb-3">
                        <label class="form-label">Дата подачи окончательных предложений</label>

                        <DateTimePickerComponent
                            change={(props) => {
                                const newDate = CreateDate(props)
                                setUpdateForm({ ...updateForm, procedure: { ...updateForm.procedure, offerDate: newDate } })


                            }}
                            value={updateForm.procedure.offerDate}
                            format="yyy-MM-dd- HH:mm:ss"
                            step={60}
                        >
                        </DateTimePickerComponent>
                    </div>

                    <div class="mb-3">
                        <label class="form-label">Дата подачи окончательных предложений +3 часа к offerDate (уснатавливается автоматически)</label>

                        <DateTimePickerComponent
                            value={updateForm.procedure.offerEndDateTime}
                            format="yyy-MM-dd- HH:mm:ss"
                            step={60}
                            readonly="true"
                        >
                        </DateTimePickerComponent>
                    </div>

                    <div class="mb-3">
                        <label class="form-label"> Дата и время рассмотрения и оценки вторых частей заявок</label>

                        <DateTimePickerComponent
                            change={(props) => {
                                const newDate = CreateDate(props)
                                setUpdateForm({ ...updateForm, procedure: { ...updateForm.procedure, requestReviewSecondPartsDateTime: newDate } })
                            }}
                            value={updateForm.procedure.requestReviewSecondPartsDateTime}
                            format="yyy-MM-dd- HH:mm:ss"
                            step={60}
                        >
                        </DateTimePickerComponent>
                    </div>
                </Form>
            </Row>
            <Button type='submit' onClick={getIdForProtocolEvents}>Test</Button>
            <CodeHighlArea code={sql} />

        </div>
    );
};

export default UpdateFrorm;