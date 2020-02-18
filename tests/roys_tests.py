# import csv
# import django
# import string
# import random
# import os
# import sys
# sys.path.append(os.path.dirname(__file__))
# django.setup()

# from io import BytesIO
# # from django.contrib.auth.models import Permission
# from saleor.product import AttributeInputType
# # from django.contrib.sites.models import Site
# # from django.core.files import File
# # from django.core.files.uploadedfile import SimpleUploadedFile
# # from django.forms import ModelForm
# # from django.test.client import Client
# # from django_countries import countries
# from PIL import Image
# from prices import Money, TaxedMoney
# from saleor.product.utils.attributes import associate_attribute_values_to_instance
# from saleor.discount import DiscountValueType
# from saleor.discount.models import Sale, Voucher, VoucherCustomer
# from saleor.product.models import (
#     Attribute,
#     AttributeTranslation,
#     AttributeValue,
#     Category,
#     Collection,
#     DigitalContent,
#     DigitalContentUrl,
#     Product,
#     ProductImage,
#     ProductTranslation,
#     ProductType,
#     ProductVariant,
# )


# def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))


# # def attribute_list() -> List[Attribute]:
# #     return list(
# #         Attribute.objects.bulk_create(
# #             [
# #                 Attribute(slug="size", name="Size"),
# #                 Attribute(slug="weight", name="Weight"),
# #                 Attribute(slug="thickness", name="Thickness"),
# #             ]
# #         )
# #     )







# def pink_attribute_value(color_attribute):  # pylint: disable=W0613
#     value = AttributeValue.objects.create(
#         slug="pink", name="Pink", attribute=color_attribute, value="#FF69B4"
#     )
#     return value


# def color_attribute_without_values(db):  # pylint: disable=W0613
#     return Attribute.objects.create(slug="color", name="Color")




# def product_2(product_type, category):
#     product_attr = product_type.product_attributes.first()
#     print(product_attr)
#     product_attr_value = product_attr.values.first()

#     product = Product.objects.create(
#         name="Roys Test product",
#         price=Money("10.00", "USD"),
#         product_type=product_type,
#         category=category,
#     )

#     associate_attribute_values_to_instance(product, product_attr, product_attr_value)

#     variant_attr = product_type.variant_attributes.first()
#     variant_attr_value = variant_attr.values.first()

#     variant = ProductVariant.objects.create(
#         product=product,
#         sku="123",
#         cost_price=Money("1.00", "USD"),
#         quantity=10,
#         quantity_allocated=1,
#     )

#     associate_attribute_values_to_instance(variant, variant_attr, variant_attr_value)
#     return product





# def product_with_multiple_values_attributes(product, product_type, category) -> Product:
#     attribute = Attribute.objects.create(
#         slug="modes", name="Available Modes", input_type=AttributeInputType.MULTISELECT
#     )

#     attr_val_1 = AttributeValue.objects.create(
#         attribute=attribute, name="Eco Mode", slug="eco"
#     )
#     attr_val_2 = AttributeValue.objects.create(
#         attribute=attribute, name="Performance Mode", slug="power"
#     )

#     product_type.product_attributes.clear()
#     product_type.product_attributes.add(attribute)

#     associate_attribute_values_to_instance(product, attribute, attr_val_1, attr_val_2)
#     return product


# def product_with_default_variant(product_type_without_variant, category):
#     product = Product.objects.create(
#         name="Test product",
#         price=Money(10, "USD"),
#         product_type=product_type_without_variant,
#         category=category,
#     )
#     ProductVariant.objects.create(
#         product=product, sku="1234", track_inventory=True, quantity=100
#     )
#     return product


# def variant(product):
#     product_variant = ProductVariant.objects.create(
#         product=product,
#         sku="SKU_A",
#         cost_price=Money(1, "USD"),
#         quantity=5,
#         quantity_allocated=3,
#     )
#     return product_variant


# def product_variant_list(product):
#     return list(
#         ProductVariant.objects.bulk_create(
#             [
#                 ProductVariant(product=product, sku="1"),
#                 ProductVariant(product=product, sku="2"),
#                 ProductVariant(product=product, sku="3"),
#             ]
#         )
#     )

# def product_type_without_variant():
#     product_type = ProductType.objects.create(
#         name="Type1", has_variants=False, is_shipping_required=True
#     )
#     return product_type


# # DONT TOUCH --------------------->
# def get_data_from_csv_vouchers(file_name):
#     customer_names_and_emails = []
#     with open(file_name) as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#             else:
#                 customer_names_and_emails.append([row[0], row[8]])
#                 print(f'\t{row[0]} address is {row[1]}, and his email is {row[8]}.')
#                 line_count += 1
#         print(f'Processed {line_count} lines.')
#     return customer_names_and_emails
    
# # DONT TOUCH --------------------->
# def voucher_customer(voucher, email):
#     return VoucherCustomer.objects.create(voucher=voucher, customer_email=email)

# # DONT TOUCH --------------------->
# def voucher_percentage(name, value):
#     return Voucher.objects.create(
#         code=name,
#         discount_value=value,
#         discount_value_type=DiscountValueType.PERCENTAGE
#     )

# # make sure to have only same amount of discount
# # DONT TOUCH --------------------->
# def create_vouchers_with_csv():
#     voucher_list = get_data_from_csv_vouchers('luxout_discount_customers.csv')
#     # for voucher in voucher_list: // for runnig on all the csv
#     voucher = voucher_list[213]
#     name = voucher[0]
#     email = voucher[1]
#     print(name, email)
#     code = id_generator(5)
#     create_voucher = voucher_percentage(code, 40)
#     add_voucher_to_customer = voucher_customer(create_voucher, email)
#     print(add_voucher_to_customer)


# def category_with_image(category_name, image):
#     return Category.objects.create(
#         name=category_name, slug="default", background_image=image
#     )

# def category(name):  
#     return Category.objects.create(name=name, slug=name)

# def categories_tree(product_type):  
#     parent = Category.objects.create(name="Parent", slug="parent")
#     parent.children.create(name="Child", slug="child")
#     child = parent.children.first()

#     product_attr = product_type.product_attributes.first()
#     attr_value = product_attr.values.first()

#     product = Product.objects.create(
#         name="Test product",
#         price=Money(10, "USD"),
#         product_type=product_type,
#         category=child,
#     )

#     associate_attribute_values_to_instance(product, product_attr, attr_value)
#     return parent



# def image():
#     img_data = BytesIO()
#     image = Image.new("RGB", size=(1, 1))
#     image.save(img_data, format="JPEG")
#     img_data.getvalue() 
#     return "products/COLLINA_ANTIQUE_GOLD.jpeg"
#     # return SimpleUploadedFile("C:\\Desktop\\luxout-test\\tests\\product_images\\COLLINA_ANTIQUE_GOLD.jpeg", img_data.getvalue())


# def product(product_type, category, product_type_name, price_list, product_pics):
#     fixed_name = product_type_name + " Fabric"
#     product = Product.objects.create(
#         name=fixed_name,
#         price=Money(price_list[0], "USD"),
#         product_type=product_type,
#         category=category,
#     )
#     image_var = product_pics[0]
#     ProductImage.objects.create(product=product, image=image_var)
#     for attribute in product_type.product_attributes.all():
#         product_attr_value = attribute.values.first()
#         associate_attribute_values_to_instance(product, attribute, product_attr_value)
#     variants_list = []
#     # if len(product_pics) > 0:
#     #     for pic in product_pics:
#     #         code = id_generator(5)
#     #         variant = ProductVariant.objects.create(
#     #             product=product,
#     #             sku=code,
#     #             cost_price=Money("1.00", "USD"),
#     #             quantity=10,
#     #             quantity_allocated=1,
#     #             )
#     #         variants_list.append(variant)
#     # for var in variants_list:
#     #     for attribute_varriant in product_type.variant_attributes.all():
#     #         variant_attr_value = attribute_varriant.values.first()
#     #         associate_attribute_values_to_instance(var, attribute_varriant, variant_attr_value)

#     return product


# # DONT TOUCH --------------------------->
# def create_attribute_with_value(attribute_name, attributes_values):  # pylint: disable=W0613
#     attribute = Attribute.objects.create(slug=attribute_name, name=attribute_name, value_required=True)
#     extracted_choices = []
#     varints_expended_data = []
#     is_variant = False
#     for attribute_value in attributes_values:
#         if attribute_value not in extracted_choices:
#             extracted_choices.append(attribute_value)
#     if len(extracted_choices) > 1:
#         is_variant = True
#     for choice in extracted_choices:
#         AttributeValue.objects.create(attribute=attribute, name=choice, slug=choice)
#     return attribute

# # DONT TOUCH --------------------------->
# def divide_categories(is_double_roller_shades, is_luxshade_dual_roller_shades, is_luxshade_roller_shades, is_slimline_dual_roller_shades, is_solar_shades, is_tailored_roman_roller_shades, is_designer_roller_shades):
#     only_the_active = []
#     shade_options = [{"type":"Double Roller Shades", "active":is_double_roller_shades},
#     {"type":"LuXshade Dual Roller", "active":is_luxshade_dual_roller_shades},
#     {"type":"LuXshade Roller Shades", "active":is_luxshade_roller_shades},
#     {"type":"SlimeLine Dual Roller", "active":is_slimline_dual_roller_shades},
#     {"type":"Solar Shades", "active":is_solar_shades},
#     {"type":"Tailored Roman", "active":is_tailored_roman_roller_shades},
#     {"type":"Designer Roller Shades", "active":is_designer_roller_shades}]
#     for shade_option in shade_options:
#         if shade_option["active"]:
#             only_the_active.append(shade_option["type"])
#     return only_the_active

# # DONT TOUCH---------------->
# def product_type(attributes_list, type_name):
#     fixed_name1 = type_name + " Fabric"
#     product_type = ProductType.objects.create(
#         name=fixed_name1, has_variants=True, is_shipping_required=True
#     )
#     for attribute in attributes_list:
#         if len(attribute.values.all()) > 1:
#             product_type.variant_attributes.add(attribute)
#         else:
#             product_type.product_attributes.add(attribute)
#     return product_type

# def get_data_from_csv_products_info(file_name):
#     products_info = []
#     with open(file_name) as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         types_of_shades_list = ["Designer Roller Shades", "Double Roller Shades", "Luxshade Dual Roller Shades", "Luxshade Roller Shades", "Slimline Dual Roller Shades", "Solar Shades", "Tailored Roman Shades"]
#         line_count = 0
#         product_type_name = ""
#         attributes_for_variants = []
#         additional_data = []
#         color_attribute_values = []
#         fabric_pic_name_values = []
#         fabric_part_attribute_values = []
#         fabric_composition_attribute_values = []
#         max_shade_width_attribute_values = []
#         weight_attribute_values = []
#         thickness_attribute_values = []
#         price_attribute_values = []
#         # is_translucent_or_sheer = []
#         # is_light_filtering = []
#         # is_dimout_or_room_darkening = []
#         # is_blackout_or_opaque = []
#         # is_commercial_or_fireretadant = []
#         # is_green_fabrics = []
#         # is_patterned = []
#         # is_stripes = []
#         # is_pollergen_or_anti_allergy = []
#         # is_moisture_resistant = []
#         # is_wipe_clean = []
#         # is_vaccum_clean = []
#         # is_uv_ray_blockage = []
#         # is_light_blocking_1_5 = []
#         # is_energy_saving_1_3 = []
#         roys_count = 0
#         category_var = category("Fabrics")
        
#         # category_designer_roller_shades = category("Designer_Roller_Shades") 
#         # category_double_roller_shades = category("Double Roller Shades") 
#         # category_luxshade_dual_roller_shades = category("Luxshade Dual Roller Shades") 
#         # category_luxshade_roller_shades = category("Luxshade Roller Shades") 
#         # category_slimline_dual_roller_shades = category("Slimline Dual Roller Shades")
#         # category_solar_shades = category("Solar Shades")
#         # category_tailored_roman_shades = Category("Tailored Roman Shades")
#         # remember to add the correct Background
#         # is_designer_roller_shades = False
#         # is_luxshade_roller_shades = False
#         # is_slimline_dual_roller_shades = False
#         # is_luxshade_dual_roller_shades = False
#         # is_double_roller_shades = False
#         # is_tailored_roman_roller_shades = False
#         # is_solar_shades = False
#         shade_options = []
#         for row in csv_reader:
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#             elif line_count > 0 and roys_count < 2:
#                 if (row[0] == ""):
                    
#                     roys_count += 1
#                     # check if there is more then 1 values and decide either varint/notchanging
#                     # shades_list = divide_categories(is_double_roller_shades, is_luxshade_dual_roller_shades, is_luxshade_roller_shades, is_slimline_dual_roller_shades, is_solar_shades, is_tailored_roman_roller_shades, is_designer_roller_shades)
#                     attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Shades-Types", list(set(shade_options))))
#                     attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Color", color_attribute_values))
#                     # attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Price", price_attribute_values))
#                     # attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Picture", fabric_pic_name_values))
#                     # attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Fabric-Part-Number", fabric_part_attribute_values))
#                     attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Fabric-Composition", fabric_composition_attribute_values))
#                     attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Max-Shade-Width", max_shade_width_attribute_values))
#                     attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Weight", weight_attribute_values))
#                     attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Thickness", thickness_attribute_values))                       
#                     print(attributes_for_variants)
#                     product_type_var = product_type(attributes_for_variants, product_type_name)
#                     print(product_type_var, "product_type_var")
#                     product(product_type_var, category_var, product_type_name, price_attribute_values, fabric_pic_name_values)
#                     color_attribute_values = []
#                     fabric_part_attribute_values = []
#                     fabric_composition_attribute_values = []
#                     max_shade_width_attribute_values = []
#                     weight_attribute_values = []
#                     thickness_attribute_values = []
#                     price_attribute_values = []
#                     fabric_pic_name_values = []
#                     attributes_for_variants = []
#                     additional_data = []
#                     shade_options = []
#                 else:
#                     product_type_name = row[0]
#                     color_attribute_values.append(row[1])
#                     fabric_part_attribute_values.append(row[2])
#                     fabric_pic_name_values.append(row[3])
#                     fabric_composition_attribute_values.append(row[4])
#                     max_shade_width_attribute_values.append(row[5])
#                     weight_attribute_values.append(row[6])
#                     thickness_attribute_values.append(row[7])
#                     price_attribute_values.append(row[8])
#                     if (row[9] == "x"):
#                         shade_options.append("Designer Roller Shades")
#                         # is_designer_roller_shades = True
#                         # designer_roller_shades.append(row[0])
#                     if (row[10] == "x"):
#                         shade_options.append("LuXshade Roller Shade")
#                         # is_luxshade_roller_shades = True
#                         # luxshade_roller_shades.append(row[0])
#                     if (row[11] == "x"):
#                         # is_slimline_dual_roller_shades = True
#                         shade_options.append("Slimline Dual Roller Shades")
#                         # slimline_dual_roller_shades.append(row[0])
#                     if (row[12] == "x"):
#                         shade_options.append("LuXshade Roller Shades")
#                         # is_luxshade_dual_roller_shades = True
#                         # luxshade_roller_shades.append(row[0])
#                     if (row[13] == "x"):
#                         shade_options.append("Double Roller Shades")
#                         # is_double_roller_shades = True
#                         # double_roller_shades.append(row[0])
#                     if (row[14] == "x"):
#                         shade_options.append("Taliolred Roman Roller Shades")
#                         # is_tailored_roman_roller_shades = True
#                         # tailored_roman_roller_shades.append(row[0])
#                     if (row[15] == "x"):
#                         shade_options.append("Solar Shades")
#                         # solar_shades.append(row[0])

#                     # is_translucent_or_sheer.append(row[27])
#                     # is_light_filtering.append(row[28])
#                     # is_dimout_or_room_darkening.append(row[29])
#                     # is_blackout_or_opaque.append(row[30])
#                     # is_commercial_or_fireretadant.append(row[31])
#                     # is_green_fabrics.append(row[32])
#                     # is_patterned.append(row[33])
#                     # is_stripes.append(row[34])
#                     # is_pollergen_or_anti_allergy.append(row[35])
#                     # is_moisture_resistant.append(row[36])
#                     # is_wipe_clean.append(row[37])
#                     # is_vaccum_clean.append(row[38])
#                     # is_uv_ray_blockage.append(row[39])
#                     # is_light_blocking_1_5.append(row[40])
#                     # is_energy_saving_1_3.append(row[41])
#                     # print(f'\t{row[0]} works in the {row[2]} department, and his email is {row[5]}.')
#                 line_count += 1
#         # shades_data = [list(set(designer_roller_shades)), list(set(luxshade_roller_shades)), list(set(slimline_dual_roller_shades)), 
#         # list(set(luxshade_dual_roller_shades)), list(set(double_roller_shades)), list(set(solar_shades))]
#         # counter = 0
#         # for shade in types_of_shades_list:
#         #     create_attribute_with_value(shade + "-Fabric Types", shades_data[counter])
#             # counter += 1
#         # shade_product_type = pro
#         # shades_products = create_shade_products(category_shades, )
#         # print (shades_products)
#         print(f'Processed {line_count} lines.')
#     return products_info


                    
# # type, name, category, sku, price
# def product_creation(product_type, category, price_fabric, sku_strings, fabric_pics, fabric_prices_by_size_list):
#     # create product
#     product = Product.objects.create(
#         name=product_type.name + "-" + category.name,
#         price=Money(price_fabric, "USD"),
#         product_type=product_type,
#         category=category,
#     )
#     for pic in fabric_pics:
#         ProductImage.objects.create(product=product, image="products\\" + pic)

#     # add image
#     # ProductImage.objects.create(product=product, image=product_picture)

#     # add attributes (equal value to all products)
#     for attribute in product_type.product_attributes.all():
#         product_attr_value = attribute.values.first()
#         associate_attribute_values_to_instance(product, attribute, product_attr_value)

#     # add variants and create all type of diffrent products
#     counter = 0
#     length_values = []
#     width_values = []
#     color_values = []
#     length_attribute = ""
#     width_attribute = ""
#     color_attribute = ""
#     varints_count = len(product_type.variant_attributes.all())
#     for attribute_varriant in product_type.variant_attributes.all():
#         for variant_value in attribute_varriant.values.all():
#             print(attribute_varriant.name, variant_value)
#             if varints_count > 2:
#                 if counter == 1:
#                     length_values.append(variant_value)
#                     length_attribute = attribute_varriant
#                 elif counter == 2:
#                     width_values.append(variant_value)
#                     width_attribute = attribute_varriant
#                 elif counter == 0:
#                     if variant_value:
#                         color_values.append(variant_value)
#                         color_attribute = attribute_varriant
#             else:
#                 if counter == 0:
#                     length_values.append(variant_value)
#                     length_attribute = attribute_varriant
#                 elif counter == 1:
#                     width_values.append(variant_value)
#                     width_attribute = attribute_varriant
#         counter += 1
#     addtional_counter = 0
#     addtional_counter2 = 0
#     print(length_attribute, length_values, "len")
#     print(width_attribute, width_values, "wid")
#     print(color_attribute, color_values, "color")
#     # if varints_count > 2:
#     #     color_index = 0
#     #     for color in color_values:
#     #         for length_value in length_values:
#     #             for width_value in width_values:
#     #                 width_value_fixed = str(width_value.name)
#     #                 length_value_fixed = str(length_value.name)
#     #                 color_value_fixed = str(color.name)
#     #                 sku_id = sku_strings[color_index] + "-" + category.name + " " + length_value_fixed + "X" + width_value_fixed
#     #                 variant = ProductVariant.objects.create(
#     #                     product=product,
#     #                     name=color_value_fixed + " " + length_value_fixed + " " + width_value_fixed,
#     #                     sku=sku_id,
#     #                     price_override=Money(fabric_prices_by_size_list[addtional_counter], "USD"),
#     #                     quantity=10,
#     #                     quantity_allocated=1,
#     #                     )   
#     #                 associate_attribute_values_to_instance(variant, color_attribute, color)
#     #                 associate_attribute_values_to_instance(variant, width_attribute, width_value)
#     #                 associate_attribute_values_to_instance(variant, length_attribute, length_value)
#     #                 addtional_counter += 1
#     #         addtional_counter = 0
#     #         color_index += 1

#     # else:
#     #     print("in Else of < 2 var count")
#     #     for length_value in length_values:
#     #             for width_value in width_values:
#     #                 width_value_fixed = str(width_value.name)
#     #                 length_value_fixed = str(length_value.name)
#     #                 rand = id_generator()
#     #                 sku_id = rand + "-" + category.name + " " + length_value_fixed + "X" + width_value_fixed
#     #                 variant = ProductVariant.objects.create(
#     #                     product=product,
#     #                     name=length_value_fixed + "X" + width_value_fixed,
#     #                     sku=sku_id,
#     #                     price_override=Money(fabric_prices_by_size_list[addtional_counter2], "USD"),
#     #                     quantity=10,
#     #                     quantity_allocated=1,
#     #                     )
#     #                 associate_attribute_values_to_instance(variant, color_attribute, color)
#     #                 associate_attribute_values_to_instance(variant, width_attribute, width_value)
#     #                 associate_attribute_values_to_instance(variant, length_attribute, length_value)
#     #                 addtional_counter2 += 1
#     #             addtional_counter2 = 0
                
#     return product

# def get_data_from_csv_shades_products(file_name, product_type_to_prices):
#     is_designer_roller_shades = False
#     is_luxshade_roller_shades = False
#     is_slimline_dual_roller_shades = False
#     is_luxshade_dual_roller_shades = False
#     is_double_roller_shades = False
#     is_tailored_roman_roller_shades = False
#     is_solar_shades = False
#     product_type_name = ""
#     color_attribute_values = []
#     fabric_part_attribute_values = []
#     fabric_composition_attribute_values = []
#     max_shade_width_attribute_values = []
#     weight_attribute_values = []
#     thickness_attribute_values = []
#     price_attribute_values = []
#     fabric_pic_name_values = []
#     attributes_for_variants = []
#     shade_to_fabric_type= []
#     shade_options = []
#     fabric_data = []
#     product_type_vars = [] #never empty
#     line_count = 0
#     roys_count = 0
#     with open(file_name) as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         for row in csv_reader:
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#             elif line_count > 0 and roys_count < 3:
#                 if (row[0] == ""):
#                     roys_count += 1
#                     fabric_data = list(filter(lambda fabric_type: fabric_type['fabric_name'] == product_type_name, product_type_to_prices))
#                     fabric_data_ready_to_read = fabric_data[0]                    
#                     print(fabric_data_ready_to_read['prices_list'], product_type_name, "prices and name")
#                     attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Color", color_attribute_values))
#                     attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Fabric-Composition", fabric_composition_attribute_values))
#                     attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Max-Shade-Width", max_shade_width_attribute_values))
#                     attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Weight", weight_attribute_values))
#                     attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Thickness", thickness_attribute_values))
#                     attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Width", fabric_data_ready_to_read['upper_values_list']))
#                     attributes_for_variants.append(create_attribute_with_value(product_type_name + "-Length", fabric_data_ready_to_read['left_values_list']))
#                     print(attributes_for_variants)
#                     product_type_vars.append({"product_type_object":product_type(attributes_for_variants, product_type_name), "fabric_type_match_to_shade":[is_designer_roller_shades,
#                     is_luxshade_roller_shades,
#                     is_slimline_dual_roller_shades,
#                     is_luxshade_dual_roller_shades,
#                     is_double_roller_shades,
#                     is_tailored_roman_roller_shades,
#                     is_solar_shades], "sku_values": fabric_part_attribute_values, "price": price_attribute_values[0], "fabric_colors_pics": fabric_pic_name_values, "fabric_prices_list_by_size":fabric_data_ready_to_read['prices_list']})

#                     is_designer_roller_shades = False
#                     is_luxshade_roller_shades = False
#                     is_slimline_dual_roller_shades = False
#                     is_luxshade_dual_roller_shades = False
#                     is_double_roller_shades = False
#                     is_tailored_roman_roller_shades = False
#                     is_solar_shades = False
#                     fabric_data = []
#                     color_attribute_values = []
#                     fabric_part_attribute_values = []
#                     fabric_composition_attribute_values = []
#                     max_shade_width_attribute_values = []
#                     weight_attribute_values = []
#                     thickness_attribute_values = []
#                     price_attribute_values = []
#                     fabric_pic_name_values = []
#                     attributes_for_variants = []
#                     shade_options = []
                
#                 else:
#                     product_type_name = row[0]
#                     color_attribute_values.append(row[1])
#                     fabric_part_attribute_values.append(row[2])
#                     fabric_pic_name_values.append(row[3])
#                     fabric_composition_attribute_values.append(row[4])
#                     max_shade_width_attribute_values.append(row[5])
#                     weight_attribute_values.append(row[6])
#                     thickness_attribute_values.append(row[7])
#                     price_attribute_values.append(row[8])
#                     if (row[9] == "x"):
#                         is_designer_roller_shades = True
#                         shade_options.append("Designer Roller Shades")
#                     if (row[10] == "x"):
#                         is_luxshade_roller_shades = True
#                         shade_options.append("LuXshade Roller Shades")
#                     if (row[11] == "x"):
#                         is_slimline_dual_roller_shades = True
#                         shade_options.append("Slimline Dual Roller Shades")
#                     if (row[12] == "x"):
#                         is_luxshade_dual_roller_shades = True
#                         shade_options.append("LuXshade Dual Roller Shades")
#                     if (row[13] == "x"):
#                         is_double_roller_shades = True
#                         shade_options.append("Double Roller Shades")
#                     if (row[14] == "x"):
#                         is_tailored_roman_roller_shades = True
#                         shade_options.append("Taliolred Roman Roller Shades")
#                     if (row[15] == "x"):
#                         is_solar_shades = True
#                         shade_options.append("Solar Shades")
#                 line_count += 1
#         print(f'Processed {line_count} lines.')
#     return product_type_vars

# def create_shades_as_categories():
#     types_of_shades_list = ["Designer Roller Shades", "Luxshade Roller Shades", "Slimline Dual Roller Shades", "Luxshade Dual Roller Shades", "Double Roller Shades", "Tailored Roman Shades", "Solar Shades"]
#     # category_var = category("Shades"
#     shade_types = []
#     counter_for_images = 0
#     for shade in types_of_shades_list:
#         if counter_for_images % 2 != 0:
#             shade_image = "category-backgrounds/shade_type_one.png"
#         else:
#             shade_image = "category-backgrounds/shade_type_two.svg"
#         # 4 every shade make category and append the category to array  
#         shade_types.append(category_with_image(shade, shade_image))
#         # switch to category with pic
#         counter_for_images += 1
#     return shade_types

# def get_data_from_csv_fabric_size_to_price(file_name):
#     with open(file_name) as csv_file:
#         fabric_name_and_prices = []
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         current_options_upper = []
#         current_options_left = []
#         prices_list = []
#         line_count = 0
#         left_var = ""
#         fabric_name = ""
#         for row in csv_reader:
#             if row[0] == "":
#                 inner_counter = 0
#                 for row_value in row:
#                     if inner_counter != 0:
#                         current_options_upper.append(row_value)
#                     else:
#                         current_options_upper = []
#                     inner_counter += 1
#                 print(current_options_upper)
#             elif (len(row[0]) >= 4):
#                 if line_count == 0:
#                     fabric_name = row[0]
#                     print(fabric_name, "First Fabric Name!!!!!!!!!")
#                 else:
#                     fabric_name_and_prices.append({"fabric_name": fabric_name,
#                     "upper_values_list":current_options_upper, "left_values_list":current_options_left, "prices_list":prices_list})
#                     print("end of product")
#                     current_options_left = []
#                     prices_list = []
#                     fabric_name = row[0]
#                     print(fabric_name, "New Product Name!!!!!!!!!")
#             else:
#                 seconed_inner_counter = 0
#                 for row_value in row:
#                     if seconed_inner_counter == 0:
#                         left_var = row_value
#                         current_options_left.append(left_var)
#                         print(row_value, "This is the left Var")
#                     elif seconed_inner_counter > 0:
#                         temp = seconed_inner_counter - 1
#                         prices_list.append(row_value)
#                         print(row_value, " is the price of ", left_var, "and", current_options_upper[temp])
#                     seconed_inner_counter += 1
#                 left_var = ""
#             line_count += 1
#         print(f'Processed {line_count} lines.')
#     return fabric_name_and_prices

# def create_products():
#     shades_as_categories = create_shades_as_categories()
#     fabric_type_to_prices = get_data_from_csv_fabric_size_to_price('tests/size_to_price.csv')
#     shade_to_fabric_type = get_data_from_csv_shades_products('tests/master_dataset.csv', fabric_type_to_prices)
#     for is_matching_fabric in shade_to_fabric_type:
#         product_type_var = is_matching_fabric["product_type_object"]
#         counter_for_keep = 0
#         for fabric_with_shade in is_matching_fabric["fabric_type_match_to_shade"]:
#             if fabric_with_shade:
#                 print(is_matching_fabric['fabric_prices_list_by_size'], "prices list------------------>")
#                 product_creation(product_type_var, shades_as_categories[counter_for_keep], is_matching_fabric["price"],
#                 is_matching_fabric["sku_values"], is_matching_fabric["fabric_colors_pics"], is_matching_fabric['fabric_prices_list_by_size'])
#             counter_for_keep += 1
            

                



# create_products()

