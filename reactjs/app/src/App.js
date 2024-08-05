// import logo from './logo.svg';
// import './App.css';
import { useState } from "react";
import RoutesApp from "./routes";
import GlobalContext from "./Context";

function App() {
  const [auth, setAuth] = useState();
  const authUserLogged = localStorage.getItem('authUserLogged');
  if (authUserLogged === null) {
    localStorage.setItem('auth', false)
  }
  return (
    <>
      <GlobalContext.Provider value={{auth, setAuth}}>
        <RoutesApp/>
      </GlobalContext.Provider>
    </>
  );
}

export default App;
