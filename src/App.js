import { useState } from "react"
function Header()
{

  return(
    <div className="header" style={{fontSize: 100, textAlign: "center"}}>
      TODO list 
    </div>
  )
}
function Footer()
{

  return(
    <div className="header" style={{fontSize: 100, textAlign: "center",bottom:0}}>
      Footer
    </div>
  )
}

function Todo({value})
{
  return(
    <div className="todocomp" style={{width:"100%",height:20}}>{value}<button >Done</button><button>Delete</button></div>
  )
}
function Todos()
{
  const [todo,setTodo]=useState()
  return(
    
    <div className="header" style={{/* width:"100%" , */height:100,backgroundColor:"red",display:"flex",alignItems:"center",justifyContent:"center"}}>
    <Todo value="market"/> 
    <Todo value="market"/> 
    <Todo value="market"/> 
    <Todo value="market"/> 
    <Todo value="market"/>
    </div>
  )
}


function App() {
  return (
    <>
      <Header/>
      <Todos/>
      <Footer/>
    </>
  )
}

export default App;