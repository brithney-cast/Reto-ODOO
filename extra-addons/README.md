En esta carpeta se incluirán los módulos de ODOO 

commands:
docker-compose up

root@c0752fd70130:/usr/bin# odoo -i custom_fields_mapping -d db_odoo -p 8001 --db_user=odoo --db_password=odoo --db_host=db_postgresql --log-level=test --test-file=/mnt/extra-addons/dv_inventory/tests/test_order.py --stop-after-init