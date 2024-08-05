import { getInstanceAxios } from "./config/config.api"

export async function getUserById(userId) {
    try {
        const instanceAxios = getInstanceAxios();
        const response = await instanceAxios.get(`/user/${userId}`);
        return response.data;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            window.location.href = '/login';
        } 
    }
}

export async function getAllUsers() {
    try {
        const instanceAxios = getInstanceAxios();
        const response = await instanceAxios.get(`/user`);
        return response.data;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            window.location.href = '/login';
        }
    }
}

/**
 * 
 * @param {*} data  {role: array, name: string, email: string, login: string, password: string, phone: string, }
 * @returns 
 */
export async function createUser(data) {
    try {
        const instanceAxios = getInstanceAxios();
        // TODO: campos
        const dataBody = {
            name: data.name,
            email: data.email,
            cpf: data.cpf,
            login: data.login,
            password: data.password,
            phone: data.phone,
            role: [data.role],
        };
        const response = await instanceAxios.post(`/user`, dataBody);
        const userCreated = response.data;
        return userCreated;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            window.location.href = '/login';
        } 
    }
}

export async function updateUser(data) {
    try {
        const instanceAxios = getInstanceAxios();
        const dataBody = {
            name:     data.name,
            email:    data.email,
            login:    data.login,
            password: data.password,
            phone:    data.phone,
            role:     [data.role],
        };
        const response = await instanceAxios.put(`/user/${data.id}`, dataBody);
        const userUpdated = response.data;
        return userUpdated;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            window.location.href = '/login';
        } 
    }
}

export async function deleteUser(userId) {
    try {
        const instanceAxios = getInstanceAxios();
        const response = await instanceAxios.delete(`/user/${userId}`);
        return response.data;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            window.location.href = '/login';
        } 
    }
}

/**
 * verificação de expiração do token JWT
 * @returns boolean
 */
export async function verifyTokenValid() {
    try {
        const authenticationToken = getAuthTokenUserLogged();
        if(!authenticationToken) {
            return false;
        }
        const instanceAxios = getInstanceAxios();
        const response = await instanceAxios.get(`/user/tokenvalid`);
        const tokenValid = response.data || false;
        return tokenValid;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            console.log("Erro 401 - não autorizado");
        } else {
            console.log("Erro ao verificar token:", error.message);
        }
        return false;
    }
}

/**
 * se tiver usuario logado retorna a string jwt
 * se nao tiver usuario logado retorna string vazia
 * @returns string jwt
 */
export const getAuthTokenUserLogged = () => {
    try {
        let jwtUser = '';
        const authUserLogged = getAuthUserLogged();
        if (authUserLogged && authUserLogged.authenticationToken) {
            jwtUser = authUserLogged.authenticationToken;
        }
        return jwtUser;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            window.location.href = '/login';
        } 
    }
}

export const getAuthUserLogged = () => {
    try {
        const authUserLogged = JSON.parse(localStorage.getItem('authUserLogged')) || '{}';
        return authUserLogged;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            window.location.href = '/login';
        } 
    }
}

export const setAuthUserLogged = async (userLogged) => {
    localStorage.setItem('authUserLogged', JSON.stringify(userLogged));
}

export const removeUserAuthLocalStorage = () => {
    localStorage.removeItem('authUserLogged');
    localStorage.setItem('auth', false);
}

/**
 * 
 * @param {string} login 
 * @param {string} password 
 * @returns boolean
 */
export const userLogin = async (login, password) => {
    try {
        let authTokenUserLogged = '';
        let authRefreshTokenUserLogged = '';
        const instanceAxios = getInstanceAxios();
        const dataBody = { username: login, password };
        const response = await instanceAxios.post(`/auth/login`, dataBody);
        authTokenUserLogged = response.data.access || '';
        authRefreshTokenUserLogged = response.data.refresh || '';
        setAuthUserLogged(response.data);
        if (!authTokenUserLogged || authTokenUserLogged === '') {
            return false;
        }
        return true;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            window.location.href = '/login';
        } 
    }
}
