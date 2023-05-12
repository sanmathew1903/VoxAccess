import React from 'react'

export default function Todo({todo}) {
  return (
    <>
      <h2>
        {todo.sno}
        {todo.task}
        
      </h2>
    </>
  )
}
