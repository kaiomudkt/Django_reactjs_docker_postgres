import { Routes, Route, BrowserRouter, Navigate } from "react-router-dom";
// import Content from "./pages/Content";
import Login from "./page/Login";
// import Profile from "./pages/Profile";
// import Users from "./pages/Users";
// import Home from "./pages/Home";
import { useContext, useState } from 'react'

function RoutesApp() {
    // const {auth, setAuth} = useContext(GlobalContext);
    // const [localAuth, setLocalAuth] = useState(Boolean(localStorage.getItem('auth')));
    // if(!localAuth) {
    //     if(location.pathname != '/login' && location.pathname != '/accessLink'){
    //         return <Navigate to="/login" />;
    //     }
    // }
    
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<Login />} />
                {/* <Route path="/" element={<Content/>} /> */}
                {/* <Route path="/profile" element={<Profile />} /> */}
                {/* <Route path="/home" element={<Home />} /> */}
                {/* <Route path="/users" element={<Users />} /> */}
                {/* <Route path="*" element={<Home/>}></Route> */}
            </Routes>
        </BrowserRouter>
    );
}

export default RoutesApp;