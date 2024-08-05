import { getInstanceAxios } from "./config/config.api"

export async function createClient(formData) {
    try {
        const instanceAxios = getInstanceAxios();
        const response = await instanceAxios.post(
            `/client`,
            formData,  
            {
                headers: { 'Content-Type': 'multipart/form-data' }
            }
        );
        const entity = response.data;
        return entity;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            window.location.href = '/login';
        }
    }
}

export async function getAllClients(data) {
    try {
        const instanceAxios = await getInstanceAxios();
        const dataBody = {
            page: data.page,
            limit: data.limit,
        }
        const response = await instanceAxios.get('/client', dataBody)
        return response.data
    } catch (error) {
        if (error.response && error.response.status === 401) {
            window.location.href = '/login';
        } 
    }
}

export async function updateClient(data) {
    try {
        const instanceAxios = getInstanceAxios();
        const linkId = data.get('id');
        const response = await instanceAxios.put(
            `/client/${linkId}`, 
            data,
            {
                headers: { 'Content-Type': 'multipart/form-data' }
            }    
        );
        const entity = response.data;
        return entity;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            window.location.href = '/login';
        }
    }
}

export async function deleteClient(data) {
    try {
        const instanceAxios = getInstanceAxios();
        const response = await instanceAxios.delete(`/client/${data.id}`);
        return response.data;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            window.location.href = '/login';
        }
    }
}
