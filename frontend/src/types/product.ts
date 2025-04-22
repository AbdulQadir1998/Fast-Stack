export interface Product {
  id: string | null;
  number: string;
  urlfriendly_number: string;
  type: string;
  barcode: string;
  name: string;
  description: string;
  sales_price: number;
  recommended_sales_price: number;
  sales_profit: number;
  cost_price: number;
  recommended_cost_price: number;
  cost_addition_percentage: number;
  min_order: number;
  min_sales: number;
  min_stock: number;
  stock_quantity: number;
  in_order_quantity: number;
  available_quantity: number;
  purchased_quantity: number;
  used_in_production_quantity: number;
  default_supplier_id: string | null;
  default_supplier: string | null;
  default_location_id: string | null;
  default_location: string | null;
  picture_url: string;
  pictures: {
    thumb: string;
    display: string;
    large: string;
    original: string;
  };
  is_barred: boolean;
  is_convertable: boolean;
  inventory_enabled: boolean;
  should_assure_quality: boolean;
  group_id: number;
  group: {
    number: number;
    name: string;
    vat_abroad: number;
    vat_eu: number;
    vat_domestic: number;
    vat_domestic_exempt: number;
    self: string;
  };
  discount_group: any | null;
  unit_id: string | null;
  unit: any | null;
  variation_id: string | null;
  variation: any | null;
  physical: {
    weight: number;
    weight_unit: string;
    height: number;
    width: number;
    depth: number;
    size_unit: string;
  };
  serial_numbers: {
    is_active: boolean;
    index: string;
  };
  batch_control: {
    is_active: boolean;
  };
  created_at: string;
  updated_at: string;
  deleted_at: string | null;
  pdf_url: string;
  department_id: string | null;
  department: any | null;
  goods_code: string;
  country_code: string;
  self: string;
}

export interface ProductsResponse {
  items: Product[];
  totalPages: number;
  totalItems: number;
  currentPage: number;
}
