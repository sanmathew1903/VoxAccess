import React from 'react'
import Todo from './Todo'
export default function Todos(props) {
    return (
        <div className='Container'>
            The todos list: 
            <Todo  todo={props.todos[0]}/>
        </div>
    )
}
