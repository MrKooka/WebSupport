import React, { useEffect, useMemo, useState } from 'react';
import procedureService from '../API/procedureService';
import { Table, Col, Button, Form, Row, ButtonGroup } from 'react-bootstrap'


import { useStatuses } from '../hooks/useStatuses';
import MyFilter from './MyFilter';
import MyTable from './MyTable';

const ShowStatuses = ({statuses, EA}) => {
    const [filter, setFilter] = useState({ sort: '', query: '' })
    const [sortedStatuses , setSortedStatuses] = useState([])
    useEffect(() => {
        setSortedStatuses(statuses.filter(status => status.type.includes(filter.sort)))
    }, [filter])
    return (
        <div>

            <Row className="justify-content-md-start mt-2 mb-4">
                <Col xs lg="2">
                    <MyFilter EA={EA} statuses={statuses} filter={filter} setFilter={setFilter} />
                </Col>
            </Row>
            <Row>
                <Col>
                    <MyTable elemsArray={sortedStatuses.length!=0?sortedStatuses:statuses} />
                </Col>
            </Row>
        </div>
    );
};

export default ShowStatuses;