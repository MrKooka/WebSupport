import React, { useState } from 'react';
import cls from './MyAccordion.module.css'
const MyAccordion = ({data}) => {
    const [visible, setVisible] = useState(false)
    const rootCls = [cls.panel]
    if (visible){
        rootCls.push(cls.active)
    }
    return (
        <div class={cls.accrodion}>
            <div class={cls.panel}>
                {data}
            </div>
                 <p>Какой то код</p>

        </div>
        
    );
};

export default MyAccordion;