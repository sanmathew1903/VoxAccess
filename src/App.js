import { useState } from "react";


function Mybutton() {
  const [count, setCount] = useState(0)
  function press() {
    setCount(count + 1)
  }

  return (
    <button onClick={press} style={{height:100,width:100}}>Button click count:{count} times .</button>

  )
}
function App() {
  return (
    <>
      <Mybutton />
      <Mybutton />
      
    </>
  )
}

export default App;