import axios from 'axios'
import { useEffect, useState } from 'react';
import { Container, FormControl, Row, Col } from 'react-bootstrap';
import MyNav from './components/MyNav';
import ShowProcedure from './components/ShowProcedure/ShowProcedure';
import CodeHighlArea from './UI/CodeHighlArea';
import Button from '@mui/material/Button';
import MyAccordion from './UI/MyAccordion/MyAccordion';
import UpdateFrorm from './UI/UpdateFrorm';
import './App.css';
import getProtocolIdCondition from './utils/getCondition';
import ReactMarkdown from 'react-markdown'
import MySideBar from './UI/MySideBar/MySideBar';
import { BrowserRouter } from "react-router-dom";
import AppRouter from './UI/AppRouter';
function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Container fluid >
        <MyNav />
        <AppRouter/>
        {/* <MySideBar/> */}
        
        {/* <Button onClick={() => { console.log(procInfo.lot.protocol.map(p => p.event && p.event)) }}>test</Button> */}
      </Container>
      </BrowserRouter>
    </div>
  );
}

export default App;
