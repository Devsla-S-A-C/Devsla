import { Helmet } from 'react-helmet-async';
import { ProductForm } from '@/components/layouts/ProductForm';

export const EditProductPage = () => {
    return (
        <>
            <Helmet>
                <title>Editar Nombre producto</title>
            </Helmet>

            <ProductForm />
        </>
    )
}
