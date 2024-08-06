import { 
    getAllSuppliers, 
    createSupplier, 
    updateSupplier, 
    deleteSupplier, 
} from "../api/supplier.api";

export function useGetAllSuppliersHook() {
    return getAllSuppliers;
}

export function useCreateSupplierHook() {
    return createSupplier;
}

export function useUpdateSupplierHook() {
    return updateSupplier;
}

export function useDeleteSupplierHook() {
    return deleteSupplier;
}
