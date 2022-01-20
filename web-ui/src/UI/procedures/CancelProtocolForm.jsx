import React, { useEffect, useState, useRef } from 'react';
import { Form, Button, Row, Col, Alert, Tabs, Tab, Table } from 'react-bootstrap';
import { DatePickerComponent } from '@syncfusion/ej2-react-calendars';
import axios from 'axios';
import procedureService from '../../API/procedureService';

const CancelProtocolForm = () => {
    const [form, setForm] = useState({
        id: [],
        controlAgency: '',
        documentName: '',
        documentNumber: '',
        decisionDate: '',
        regNum: ''

    })
    const radio = useRef(null)
    const [prorocols, setProtocols] = useState([])
    // const [packetIds, setPacketIds] = useState([])
    const [errAlert, setErrAlert] = useState(false)
    const sendForm = (e) => {
        e.preventDefault()
        checkBoxSetFalse()
        setProtocols([])
        if (form.decisionDate !== '') {
            axios.post('http://127.0.0.1:8000/api/44ek/cancelprotocol', form)
                .then((response) => {
                    console.log(response);
                })
            setForm({ id: '', controlAgency: '', documentName: '', documentNumber: '', decisionDate: '',regNum:'' })
            setErrAlert(false)
        } else {
            setErrAlert(true)
        }

    };

    const getIdFormCheckbox = (id, checked) => {
        if (checked) {
            setForm({ ...form, id: [...form.id, id] })

        } else {
            // Удаление из массива
            // https://www.delftstack.com/ru/howto/javascript/javascript-remove-from-array-by-value/
            if (form.id.length > 0) {
                let newArray = form.id.filter(function (f) { return f !== id })
                setForm({ ...form, id: [...newArray] })
            }

        }

    }
    const loadProtocols = (regNum) => {
        setForm({ ...form, id: [] })

        let res = procedureService.loadProtocols(regNum)
        res.then(res => setProtocols(res))
    }
    useEffect(() => {
        console.log('form.id:', form.id);
        console.log(prorocols);

        // console.log('Rradio.current', radio.current);

    }, [prorocols])
   
   
    const checkBoxSetFalse = () => {
        if (prorocols.length > 0) {
            let tbody = radio.current.childNodes[1]
            tbody.childNodes.forEach(element => {
                let innerDiv = element.childNodes[0]
                let checkBox = innerDiv.childNodes[0]
                checkBox.checked=false
            });
        }
    };
    return (
        <Row className='justify-content-center mx-auto' >

            <Col className='col-6'>
                <Tabs defaultActiveKey="profile" id="uncontrolled-tab-example" className="mb-3">
                    <Tab eventKey="home" title="По id протокола">
                        <Form onSubmit={sendForm}>
                            <Form.Group className="mb-3" controlId="formBasicEmail">
                                <Form.Label>id протокола</Form.Label>
                                <Form.Control required value={form.id} type="text" onChange={(e) => {
                                    const re = /^[0-9\b]+$/;
                                    if (e.target.value === '' || re.test(e.target.value)) {
                                        setForm({ ...form, id: e.target.value })
                                    }
                                }
                                } />
                            </Form.Group>
                            <Form.Group className="mb-3" controlId="formBasicEmail">
                                <Form.Label>Контролирующий орган</Form.Label>
                                <Form.Control required type="text" value={form.controlAgency} onChange={(e) => setForm({ ...form, controlAgency: e.target.value })} />
                            </Form.Group>

                            <Form.Group className="mb-3" controlId="formBasicPassword">
                                <Form.Label>Наименование документа</Form.Label>
                                <Form.Control required type="text" value={form.documentName} onChange={(e) => setForm({ ...form, documentName: e.target.value })} />
                            </Form.Group>
                            <Form.Group required className="mb-3" controlId="formBasicCheckbox">
                                <Form.Label>Номер документа</Form.Label>
                                <Form.Control required type="text" value={form.documentNumber} onChange={(e) => setForm({ ...form, documentNumber: e.target.value })} />
                            </Form.Group>
                            <Form.Group required className="mb-3" controlId="formBasicCheckbox">
                                {errAlert && <Alert variant='danger'>Забыли указать дату принятия решения КО</Alert>}
                                <Form.Label>Дата принятия решения КО</Form.Label>
                                <DatePickerComponent
                                    onChange={(e) => {
                                        if (e.target.value) {
                                            let oldDate = Date.parse(e.target.value)
                                            const newDate = new Date(oldDate).toISOString().slice(0, 10).replace('T', ' ').replace('Z', '')
                                            setForm({ ...form, decisionDate: newDate })
                                        }
                                    }}
                                    value={form.decisionDate}
                                    format="yyy-MM-dd"
                                    step={60}
                                />
                            </Form.Group>


                            <Button variant="primary" type="submit">
                                Submit
                            </Button>
                        </Form>
                    </Tab>
                    <Tab eventKey="profile" title="По номеру закупки">
                        <Form onSubmit={sendForm}>

                            <Form.Group className="mb-3" controlId="formBasicEmail">
                                <Form.Label>Номер закупки</Form.Label>
                                <Form.Control required value={form.regNum} type="text" onChange={(e) => {
                                    const re = /^[0-9\b]+$/;
                                    if (e.target.value === '' || re.test(e.target.value)) {
                                        setForm({ ...form, regNum: e.target.value })
                                    }
                                }
                                } />
                                {/* <Button onClick={onButtonClick}>test</Button> */}

                            </Form.Group>
                            <Button variant="primary" onClick={() => { loadProtocols(form.regNum) }}>
                                Загрузить
                            </Button>
                            {prorocols.length > 0 &&
                                <Table striped bordered hover ref={radio}>
                                    <thead>
                                        <tr>
                                            <th>Выбрано</th>
                                            <th>id</th>
                                            <th>Тип протокола</th>
                                        </tr>
                                    </thead>
                                    <tbody>

                                        {prorocols.length >0 && prorocols.map(p =>
                                            <tr >
                                                <Form.Check
                                                    type='checkbox'
                                                    onChange={(e) => { getIdFormCheckbox(e.target.value, e.target.checked) }}
                                                    value={p.id}
                                                    key={p.id}

                                                />
                                                <td>{p.id}</td>

                                                <td>{p.typeid.title}</td>
                                            </tr>
                                        )}


                                    </tbody>
                                </Table>
                            }
                            {form.id.length !== 0
                                &&
                                <div>
                                    <Form.Group className="mb-3" controlId="formBasicEmail">
                                        <Form.Label>id протокола</Form.Label>
                                        <Form.Control disabled required value={form.id} type="text" onChange={(e) => {
                                            const re = /^[0-9\b]+$/;
                                            if (e.target.value === '' || re.test(e.target.value)) {
                                                setForm({ ...form, id: e.target.value })
                                            }
                                        }
                                        } />
                                    </Form.Group>
                                    <Form.Group className="mb-3" controlId="formBasicEmail">
                                        <Form.Label>Контролирующий орган</Form.Label>
                                        <Form.Control required type="text" value={form.controlAgency} onChange={(e) => setForm({ ...form, controlAgency: e.target.value })} />
                                    </Form.Group>

                                    <Form.Group className="mb-3" controlId="formBasicPassword">
                                        <Form.Label>Наименование документа</Form.Label>
                                        <Form.Control required type="text" value={form.documentName} onChange={(e) => setForm({ ...form, documentName: e.target.value })} />
                                    </Form.Group>
                                    <Form.Group required className="mb-3" controlId="formBasicCheckbox">
                                        <Form.Label>Номер документа</Form.Label>
                                        <Form.Control required type="text" value={form.documentNumber} onChange={(e) => setForm({ ...form, documentNumber: e.target.value })} />
                                    </Form.Group>
                                    <Form.Group required className="mb-3" controlId="formBasicCheckbox">

                                        {errAlert && <Alert variant='danger'>Забыли указать дату принятия решения КО </Alert>}
                                        <Form.Label>Дата принятия решения КО</Form.Label>
                                        <DatePickerComponent
                                            onChange={(e) => {
                                                if (e.target.value) {
                                                    let oldDate = Date.parse(e.target.value)
                                                    const newDate = new Date(oldDate).toISOString().slice(0, 10).replace('T', ' ').replace('Z', '')
                                                    setForm({ ...form, decisionDate: newDate })
                                                }
                                            }}
                                            value={form.decisionDate}
                                            format="yyy-MM-dd"
                                            step={60}
                                        />
                                    </Form.Group>
                                    <Button variant="primary" type="submit">
                                        Отменить
                                    </Button>
                                </div>
                            }



                        </Form>
                    </Tab>
                </Tabs>

            </Col>
        </Row >
    );
};

export default CancelProtocolForm;