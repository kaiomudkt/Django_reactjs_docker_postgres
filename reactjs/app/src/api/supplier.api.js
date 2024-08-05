import { getInstanceAxios } from "./config/config.api"

export async function createSupplier(formData) {
    try {
        const instanceAxios = getInstanceAxios();
        const response = await instanceAxios.post(
            `/supplier`,
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

export async function getAllSupplier(data) {
    try {
        const instanceAxios = await getInstanceAxios();
        const dataBody = {
            page: data.page,
            limit: data.limit,
        }
        const response = await instanceAxios.get('/supplier', dataBody)
        return response.data
    } catch (error) {
        if (error.response && error.response.status === 401) {
            window.location.href = '/login';
        } 
    }
}

export async function updateSupplier(data) {
    try {
        const instanceAxios = getInstanceAxios();
        const linkId = data.get('id');
        const response = await instanceAxios.put(
            `/supplier/${linkId}`, 
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

export async function deleteSupplier(data) {
    try {
        const instanceAxios = getInstanceAxios();
        const response = await instanceAxios.delete(`/supplier/${data.id}`);
        return response.data;
    } catch (error) {
        if (error.response && error.response.status === 401) {
            window.location.href = '/login';
        }
    }
}
