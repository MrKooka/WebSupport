import React from 'react';
import  SyntaxHighlighter  from 'react-syntax-highlighter';
import { anOldHope } from 'react-syntax-highlighter/dist/esm/styles/hljs';
const CodeHighlArea = ({code}) => {
    return (
      <SyntaxHighlighter className='mt-3' language="sql" style={anOldHope}>
        {code}
      </SyntaxHighlighter>
    );
    
};

export default CodeHighlArea;