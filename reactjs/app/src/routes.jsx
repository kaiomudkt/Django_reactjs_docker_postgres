import { Routes, Route, Navigate, useLocation } from "react-router-dom";
// import Content from "./pages/Content";
import Login from "./page/Login";
// import Profile from "./pages/Profile";
// import Users from "./pages/Users";
import Home from "./page/Home";
import { useState, useEffect } from 'react'

function RoutesApp() {
    const location = useLocation();
    const [localAuth, setLocalAuth] = useState(localStorage.getItem('auth') === 'true');
    useEffect(() => {
        setLocalAuth(localStorage.getItem('auth') === 'true');
    }, [localStorage.getItem('auth')]);
    if(!localAuth && location.pathname != '/login') {
        return <Navigate to="/login" replace />;
    }
    
    return (
            <Routes>
                <Route path="/login" element={<Login />} />
                {/* <Route path="/" element={<Content/>} /> */}
                {/* <Route path="/profile" element={<Profile />} /> */}
                {/* <Route path="/home" element={<Home />} /> */}
                {/* <Route path="/users" element={<Users />} /> */}
                {<Route path="*" element={<Home/>}></Route>}
            </Routes>
    );
}

export default RoutesApp;