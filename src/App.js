
import './App.css';

import Header from './MyComp/Header'
import Footer from './MyComp/Footer';
import Todo from './MyComp/Todo';
import Todos from './MyComp/Todos';
function App() {

  let todos=[
    {
      sno: 1,
      task:"go to school"
    },
    {
      sno :2,
      task:"go to easy store"
    },
    {
      sno :3,
      task:"go to the ground"
    }

  ]
  return (
    <>
      <Header />
      <Todos todos/>
      <Todo />
      <Footer />
    </>
  );
}

export default App;
