import React from 'react';
import { Nav, Navbar, Container, NavDropdown } from 'react-bootstrap';
import {Link } from "react-router-dom";
const MyNav = () => {
    return (
        <Navbar  bg="dark" variant="dark">
            <Container>
            <Navbar.Brand className='mr-3' href="#home">Navbar</Navbar.Brand>
            <Nav className="me-auto">
                <NavDropdown title="44ЭK" id="basic-nav-dropdown">
                <NavDropdown.Item ><Link to='44ek/statuses'>Статусы</Link></NavDropdown.Item>
                <NavDropdown.Item><Link to='/44ek/updateForm'>Смена статуса 44ЭК</Link></NavDropdown.Item>
                <NavDropdown.Item><Link to='/44ek/cancelprotocol'>Отмена протокола</Link></NavDropdown.Item>

                    
                </NavDropdown>
                <NavDropdown title="44ЭA" id="basic-nav-dropdown">
                    <NavDropdown.Item ><Link to='44ea/statuses'>Статусы</Link></NavDropdown.Item>
                    <NavDropdown.Item>Смена статуса 44ЭА</NavDropdown.Item>
                </NavDropdown>
                <NavDropdown title="ELK" id="basic-nav-dropdown">
                    <NavDropdown.Item ><Link to='elk/mergeusers'>Объединение пользователей</Link></NavDropdown.Item>
                </NavDropdown>
                <NavDropdown title="Статьи" id="basic-nav-dropdown">
                    <NavDropdown.Item ><Link to='articles'>Все статьи</Link></NavDropdown.Item>

                </NavDropdown>

                
                
                <NavDropdown title="Статьи" id="basic-nav-dropdown">
                    <NavDropdown.Item ><Link to='erdiag'>ER</Link></NavDropdown.Item>

                </NavDropdown>
            </Nav>
            </Container>
        </Navbar>
    );
};

export default MyNav;