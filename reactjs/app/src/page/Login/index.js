import React, { useState } from 'react'
import { useGetUserLoginHook, useRemoveAuthLocalStorageHook } from '../../hook/user.hook';
import './style.css'

export default function Login() {
    const [login, setLogin] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const removeUserAuthLocalStorage = useRemoveAuthLocalStorageHook();
    removeUserAuthLocalStorage();
    const handleAuth = async () => {
        // if(!login || !password) {
        //     setErrorMessage("Preencha todos os campos!");
        //     return;
        // }
        // const authenticatedBool = await useGetUserLoginHook(login, password);
        // const { data, error } = await useGetUserLoginHook(login, password);
        // if(authenticatedBool === true) {
        //     localStorage.setItem('auth', true)
        //     window.location.href = '/';
        // } else {
        //     localStorage.setItem('auth', false)
        //     setErrorMessage("Usuário ou senha incorretos!");
        //     return;
        // }
    }

    return (
        <div className='area-login'>
            <div className='login'>
                <span>Clarke</span>
                <label>{errorMessage}</label>
                <div className="formulario">
                    <input
                        type="text"
                        name='nome'
                        placeholder='Nome de Usuário'
                        value={login}
                        onChange={(element) => {
                            setLogin(element.target.value)
                            setErrorMessage("")
                        }}
                    />
                    <input
                        type="password"
                        name='senha'
                        placeholder='Senha'
                        value={password}
                        onChange={(element) => {
                            setPassword(element.target.value)
                            setErrorMessage("")
                        }}
                    />
                    <button className='signin' onClick={handleAuth}>Entrar</button>
                </div>
            </div>
        </div>
    )
}