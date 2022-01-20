import React from 'react';
import { Table } from 'react-bootstrap'

const MyTable = ({elemsArray}) => {
    console.log('elemsArray',elemsArray);
    const TableHeader = ({ elems }) => {
        if (elems) {
            return Object.keys(elems).map((_, index) => (<th key={index}>{_}</th>))
        }
        return <div></div>
    }
    
    const TableRwo = ({elem}) => {
        return <tr>{Object.values(elem).map(v => <td>{v}</td>)}</tr>

    }

    return (
        <div>
            <Table striped bordered hover>
                <thead>
                    <TableHeader elems={elemsArray[0]} />
                </thead>
                <tbody>
                    {elemsArray.map(element => <TableRwo elem={element}/>)}
                </tbody>
            </Table>
        </div>
    );
};

export default MyTable;