import React, { useState, useEffect } from 'react';
import styled from "styled-components";
import { Link, Navigate, useNavigate } from 'react-router-dom';
import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import { RiReplyAllFill } from "react-icons/ri";
import SidebarMenu from "../sidebarMenu.js";
import { IconContext } from "react-icons";
import { useGetUserLoggedHook, useRemoveAuthLocalStorageHook } from '../../hook/user.hook.js';

const Nav = styled.div`
    background: #fff;
    height: 80px;
    display: flex;
    justify-content: space-between;
    align-items: center;
`

const NavIcon = styled.div`
    margin-left: 2rem;
    font-size: 2rem;
    height: 80px;
    display: flex;
    justify-content: flex-start;
    align-items: center;
`

const SideBadNav = styled.nav`
    background: #fff;
    width: 250px;
    height: 100vh;
    display: flex:
    justify-content: center;
    position: fixed;
    border-right: 1px solid rgb(221, 221, 221);
    overflow: auto;
    top: 0;
    left: ${({ sideBar }) => (sideBar ? '0' : '-100%')};
    transition: 450ms;
    z-index: 11;
`

const SideBarPrincipal = styled.nav`
    background: #fff;
    width: 250px;
    height: 100vh;
    display: flex:
    justify-content: center;
    position: fixed;
    border-right: 1px solid rgb(221, 221, 221);
    top: 0;
    left: ${({ sidebarPrincipal }) => (sidebarPrincipal ? '0' : '-100%')};
    transition: 450ms;
    z-index: 9;
`

const SideBarNavItens = styled.div`
    width: 100%;

`

const SideBarNavItensPrincipal = styled.div`
    display: flex;
    flex-direction: column;
`

const MeusDados = styled.p`
    color: #2f2f2f;
    font-size: 15px;
    font-weight: bold;
    letter-spacing: 1px;
    padding: 20px;
`

const ItemSidebarPrincipal = styled(Link)`
    color: #2f2f2f;
    font-size: 15px;
    font-weight: bold;
    padding: 20px;
    text-decoration: none;
    display: flex;
    align-items: center;

    &:hover {
        background-image: linear-gradient(to right, #fff, rgb(128, 192, 255));
        border-right: 5px solid rgb(16, 94, 172);
    }
`

const LogoName = styled(Link)`
    font-size: 25px;
    font-weight: bold;
    padding: 20px;
    color: rgb(16, 94, 172);
    text-decoration: none;
`

const CreateNewSidebarMenu = styled.button`
    width: 100%;
    border: none;
    height: 50px;
    background-color: rgb(16, 94, 172);
    color: #fff;
    font-size: 15px;

    &:hover {
        background-color: rgb(30, 110, 191);
        color: #fff;
        cursor: pointer;
    }
`

const UpdateItemMenu = styled.button`
    width: 100%;
    border: none;
    height: 50px;
    background-color: rgb(16, 94, 172);
    color: #fff;
    font-size: 15px;

    &:hover {
        background-color: rgb(30, 110, 191);
        color: #fff;
        cursor: pointer;
    }
`

const UpdateSidebarLink = styled.button`
    width: 100%;
    border: none;
    height: 50px;
    background-color: rgb(16, 94, 172);
    color: #fff;
    font-size: 15px;

    &:hover {
        background-color: rgb(30, 110, 191);
        color: #fff;
        cursor: pointer;
    }
`

const CreateNewAccessLinkCard = styled.button`
    width: 100%;
    border: none;
    height: 50px;
    background-color: rgb(32, 174, 32);
    color: #fff;
    font-size: 15px;

    &:hover {
        background-color: rgb(53, 200, 53);
        color: #fff;
        cursor: pointer;
    }
`

const Info = styled.div`
`

const ExitHome = {
    color: '#2f2f2f',
    textDecoration: 'none',
    marginRight: '2rem'
}

const Profile = {
    color: '#2f2f2f',
    textDecoration: 'none',
    marginRight: '2rem',
}

const Cursor = {
    cursor: 'pointer'
}

const IconNavPrincipal = {
    marginRight: '1rem',
    fontSize: '25px'
}

const PainelAdmin = {
    color: '#2f2f2f',
    textDecoration: 'none',
    marginRight: '2rem',
    fontWeight: 'bold'
}

const Unlogged = {
    marginTop: '30px'
}

function Sidebar(props) {
    const { setMenuId } = props;
    // const location = useLocation();
    const [itensMenu, setItensMenu] = useState([]);
    const [userLogged, setUserLogged] = useState(useGetUserLoggedHook());
    const [authenticate, setauthenticate] = useState(localStorage.getItem('auth') == 'true');
    const [sidebarPrincipal, setSidebarPrincipal] = useState(localStorage.getItem('auth') == 'true');
    const showSidebarPrincipal = () => setSidebarPrincipal(!sidebarPrincipal);
    const [sidebar, setSidebar] = useState(!(localStorage.getItem('auth') == 'true'));
    const showUserName = userLogged ? Object.keys(userLogged).length !== 0 : false;
    const navigate = useNavigate();

    const showSidebar = () => {
        setSidebar(!sidebar);
        setSidebarPrincipal(!sidebarPrincipal);
    };
    const Signout = () => {
        const removeUserAuthLocalStorage = useRemoveAuthLocalStorageHook();
        removeUserAuthLocalStorage();
        // navigate('/accessLink');
        window.location.reload();
    }

    useEffect(() => {
        // async function fetchMenus() {
        //     const menus = await useGetAllMenusHook();
        //     setItensMenu(menus);
        // }
        // fetchMenus();

        // function fetchMostramenuprincipal () {
        //     if(location.pathname == '/accessLink') {
        //         setSidebarPrincipal(false);
        //     }
        // }
        // fetchMostramenuprincipal();
    }, []);

    return (
            <>
                <IconContext.Provider value={{ color: 'rgb(16, 94, 172)' }}>
                    <Nav>
                        <NavIcon>
                            <FaIcons.FaBars onClick={showSidebarPrincipal} style={Cursor} />
                            <LogoName to='/'>Clarke</LogoName>
                        </NavIcon>
                        <Info>
                            {authenticate && (<Link style={PainelAdmin} to='/admin/user'>Usuários</Link>)}
                            {authenticate && (<Link style={Profile} to='/profile'>{showUserName ? userLogged.userName:'b'}</Link>)}
                            {
                                authenticate ?
                                    (<Link onClick={Signout} to='/accessLink' style={ExitHome}>Sair</Link>) :
                                    (<Link to='/login' style={ExitHome}>Entrar</Link>)
                            }
                        </Info>
                    </Nav>
                    {
                        sidebarPrincipal && authenticate && 
                        (
                            <SideBarPrincipal sidebarPrincipal={sidebarPrincipal}>
                                <SideBarNavItensPrincipal>
                                    <NavIcon to='#'>
                                        <AiIcons.AiOutlineClose onClick={showSidebarPrincipal} style={Cursor} />
                                    </NavIcon>
                                    <MeusDados>Meus Dados</MeusDados>
                                    <ItemSidebarPrincipal to='/home'><AiIcons.AiFillHome style={IconNavPrincipal} />Home</ItemSidebarPrincipal>
                                    {authenticate && (<ItemSidebarPrincipal to='/supplier'><AiIcons.AiOutlineUser style={IconNavPrincipal} />Fornecedores</ItemSidebarPrincipal>)}
                                    <ItemSidebarPrincipal onClick={showSidebar} to='/client'><RiReplyAllFill style={IconNavPrincipal} />Clientes</ItemSidebarPrincipal>
                                </SideBarNavItensPrincipal>
                            </SideBarPrincipal>
                        )
                    }
                    {
                        (
                            <SideBadNav sideBar={sidebar}>
                                <SideBarNavItens>
                                    {authenticate ? (
                                        <>
                                            <NavIcon to='#'>
                                                <AiIcons.AiOutlineArrowLeft onClick={showSidebar} style={Cursor} />
                                            </NavIcon>
                                            <MeusDados>Links de Acesso</MeusDados>
                                        </>
                                    ) : (
                                        <MeusDados style={Unlogged}>Links de Acesso</MeusDados>
                                    )}
                                    {itensMenu.map((item, index) => {
                                        return <SidebarMenu setMenuId={setMenuId} item={item} key={index} marginLeft={20} background={'#fff'} />;
                                    })}
                                </SideBarNavItens>
                            </SideBadNav>
                        )
                    }
                </IconContext.Provider>
            </>
        )

}

export default Sidebar;
