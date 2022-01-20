import axios from 'axios';
import React, { useEffect, useState } from 'react';
import ReactMarkdown from 'react-markdown'
import { Col, Row } from 'react-bootstrap'
import SyntaxHighlighter from 'react-syntax-highlighter';
import { monokai } from 'react-syntax-highlighter/dist/esm/styles/hljs';

const ShowArticles = () => {
    const [article, setArticle] = useState({})
    useEffect(() => {
        let res = axios.get('http://127.0.0.1:8000/api/articles/')
        res.then(res => console.log(res.data.test))
        res.then(res => setArticle(res.data.test))
    }, [])

    return (
        <div>
            <Row className='justify-content-center'> 
                <Col className='col-6'>
                    <ReactMarkdown
                        children={article}
                        components={{
                            code({ node, inline, className, children, ...props }) {
                                const match = /language-(\w+)/.exec(className || '')
                                console.log(match);
                                return !inline && match ? (
                                    <SyntaxHighlighter
                                        children={String(children).replace(/\n$/, '')}
                                        style={monokai}
                                        language={match[1]}
                                        PreTag="div"
                                        {...props}
                                    />
                                ) : (
                                    <code className={className} {...props}>
                                        {article}
                                    </code>
                                )
                            }
                        }}
                    />
                </Col>
            </Row>

        </div>
    );
};

export default ShowArticles;