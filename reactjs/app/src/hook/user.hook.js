import { 
    getAllUsers, 
    createUser, 
    updateUser, 
    deleteUser, 
    getAuthTokenUserLogged, 
    userLogin, 
    getAuthUserLogged, 
    removeUserAuthLocalStorage, 
    verifyTokenValid } from "../api/user.api";
import { useState } from 'react';

    
export const useGetUserLoginHook = () => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const authenticate = async (login, password) => {
        // setLoading(true);
        try {
            // const response = await axios.post('/auth/login', { login, password });
            // setLoading(false);
            // return response.data.authenticated; // Ou o que você espera que a API retorne
            return await userLogin(login, password);
        } catch (error) {
            // setLoading(false);
            setError(error);
            return false;
        }
    };

    return { authenticate, loading, error };
};
// export async function useGetUserLoginHook(login, password) {
//     const [loading, setLoading] = useState(false);
//     const [error, setError] = useState(null);
//     return await userLogin(login, password);
// }

export async function useGetAuthUserLoggedHook() {
    return getAuthTokenUserLogged();
}

export function useGetUserLoggedHook() {
    return getAuthUserLogged();
}

export function useRemoveAuthLocalStorageHook() {
    return removeUserAuthLocalStorage;
}

export function useVerifyTokenValidHook() {
    return verifyTokenValid;
}

export async function useGetAllUsersHook() {
    return await getAllUsers();
}

export function useCreateUserHook() {
    return createUser;
}

export function useUpdateUserHook() {
    return updateUser;
}

export function useDeleteUserHook() {
    return deleteUser;
}
