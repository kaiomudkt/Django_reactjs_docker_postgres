// import logo from './logo.svg';
// import './App.css';
import { useState } from "react";
import RoutesApp from "./routes";
import GlobalContext from "./Context";
import { BrowserRouter } from 'react-router-dom';

function App() {
  const [auth, setAuth] = useState();
  const authUserLogged = localStorage.getItem('authUserLogged');
  if (authUserLogged === null) {
    localStorage.setItem('auth', false)
  }
  return (
    <>
      <BrowserRouter>
        <GlobalContext.Provider value={{ auth, setAuth }}>
          <RoutesApp />
        </GlobalContext.Provider>
      </BrowserRouter>
    </>
  );
}

export default App;
