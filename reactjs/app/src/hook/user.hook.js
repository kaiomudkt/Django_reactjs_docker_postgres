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

export async function useGetUserLoginHook(login, password) {
    return await userLogin(login, password);
}

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
