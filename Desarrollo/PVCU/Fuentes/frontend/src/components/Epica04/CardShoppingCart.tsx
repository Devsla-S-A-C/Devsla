import React, { useState } from "react";
import { X, Star, Minus, Plus } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { ProductCart } from "../../helpers/getProducCart";
import { useCart } from "../../hooks/useCart"; // Para manejar el carrito

interface CardShoppingCartProps {
  product: ProductCart;
}

export const CardShoppingCart: React.FC<CardShoppingCartProps> = ({ product }) => {
  const { removeItem } = useCart(); // Para eliminar un producto del carrito
  const [quantity, setQuantity] = useState(1); // Controlar cantidad localmente

  const incrementQuantity = () => setQuantity((prev) => prev + 1);
  const decrementQuantity = () => setQuantity((prev) => Math.max(1, prev - 1));

  return (
    <Card>
      <CardContent className="p-0 flex">
        <div className="w-1/3">
          <img
            src={product.productUrl || "placeholder.jpg"} // Mostrar placeholder si no hay imagen
            alt={product.productTitle}
            className="w-full h-full object-cover"
          />
        </div>
        <div className="w-2/3 py-3 px-5 space-y-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center justify-center text-white bg-[#FBC116] rounded-3xl w-[68px] py-1 px-4">
              <Star className="w-3 h-3 fill-white" />
              <span className="text-xs font-sans ml-1">{product.productRating.toFixed(1)}</span>
            </div>
            <Button
              size="icon"
              onClick={() => removeItem(product.productTitle)}
              className="rounded-full bg-white text-terciaryLight hover:bg-white hover:shadow-xl"
            >
              <X className="h-4 w-4" />
            </Button>
          </div>
          <div className="space-y-2 font-sans">
            <span className="text-secondaryLight text-xl font-bold">{product.productTitle}</span>
            <p className="text-gray-600 text-base font-semibold">Precio: S/ {product.productPrice.toFixed(2)}</p>
            <p className="text-sm text-gray-500">{product.productDescription}</p>
          </div>
          <div className="flex justify-between items-center">
            <p className="text-xl font-semibold items-center">S/ {(product.productPrice * quantity).toFixed(2)}</p>
            <div className="flex items-center justify-around gap-4">
              <Button
                variant="counter"
                size="icon"
                onClick={decrementQuantity}
                className="h-8 w-8"
              >
                <Minus className="h-4 w-4" />
              </Button>
              <span className="text-xl font-semibold px-3">{quantity}</span>
              <Button
                variant="counter"
                size="icon"
                onClick={incrementQuantity}
                className="h-8 w-8"
              >
                <Plus className="h-4 w-4" />
              </Button>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  );
};
