from rest_framework import serializers
from .models import Vendor,PurchaseOrder,HistoricalPerformance 

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name', 'vendor_code', 'contact_details', 'address']


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['po_number', 'vendor', 'order_date','delivery_date','items', 
                  'quantity', 'status', 'quality_rating',  'issue_date', 'acknowledgment_date']     

class PerfomanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = ['name', 'vendor_code', 'on_time_delivery_rate', 'quality_rating_avg',
                  'average_response_time', 'fulfillment_rate']  

class AcknowledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = ['acknowledgment_date']


