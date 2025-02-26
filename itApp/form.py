from django import forms
from .models import *

class ComputersForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = '__all__'
        widgest = {
            'comid': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'processor': forms.TextInput(attrs={'class': 'form-control'}),
            'graphic': forms.TextInput(attrs={'class': 'form-control'}),
            'display': forms.TextInput(attrs={'class': 'form-control'}),
            'ram': forms.TextInput(attrs={'class': 'form-control'}),
            'Storage': forms.TextInput(attrs={'class': 'form-control'}),
            'OS': forms.TextInput(attrs={'class': 'form-control'}),
            'battery': forms.TextInput(attrs={'class': 'form-control'}),
            'warranty': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'min': '1', 'step': '0.25'}),
            'net': forms.TextInput(attrs={'class': 'form-control','min': '0'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'warranty': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labes = {
            # คอมกับโน๊ตบุ๊ค
            'comid': 'รหัสสินค้า',
            'name': 'ชื่อสินค้า',
            'model': 'รุ่น',
            'brand': 'ยี่ห้อ',
            'processor': 'ชิปประมวลผล',
            'graphic': 'การ์ดจอ',
            'display': 'ขนาดจอ',
            'ram': 'หน่วยความจำแรม',
            'Storage': 'หน่วยความจำ',
            'OS': 'ระบบปฏิบัติการ',
            'battery': 'แบตเตอรี่',
            'warranty': 'ประกัน',
            'weight': 'น้ำหนัก',
            'price': 'ราคา',
            'description': 'รายละเอียด',
            'net': 'คงเหลือ',
            'image': 'รูปภาพ',
            'warranty': 'ประกัน',
            'category': 'ประเภทสินค้า',
        }
    def setForUpdate(self):
        self.fields['comid'].widget.attrs['readonly'] = True
        self.fields['comid'].widget.attrs['style'] = 'background-color: #f9f9f9;'
        self.fields['comid'].label = 'รหัสสินค้า (ไม่สามารถแก้ไขได้)'
        
    class AccessoriesForm(forms.Modelform):
         class Meta:
            model = Accessories
            fields = '__all__'
            widgest = {
                'accid': forms.TextInput(attrs={'class': 'form-control'}),
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'model': forms.TextInput(attrs={'class': 'form-control'}),
                'brand': forms.TextInput(attrs={'class': 'form-control'}),
                'color': forms.TextInput(attrs={'class': 'form-control'}),
                'keyswitch': forms.TextInput(attrs={'class': 'form-control'}),
                'keypresslifetime': forms.TextInput(attrs={'class': 'form-control'}),
                'numberkey': forms.TextInput(attrs={'class': 'form-control'}),
                'mediakey': forms.TextInput(attrs={'class': 'form-control'}),
                'interface': forms.TextInput(attrs={'class': 'form-control'}),
                'size': forms.IntegerField(attrs={'class':'form-control','min': '0'}),
                'description': forms.TextInput(attrs={'class': 'form-control'}),
                'image': forms.FileInput(attrs={'class': 'form-control'}),
                'weight': forms.TextInput(attrs={'class': 'form-control'}),
                'price': forms.TextInput(attrs={'class': 'form-control', 'min': '1', 'step': '0.25'}),
                'net': forms.TextInput(attrs={'class': 'form-control','min': '0'}),
                'warranty': forms.TextInput(attrs={'class': 'form-control'}),
                'category': forms.Select(attrs={'class': 'form-control'}),
            }
            labes = {
                # เมาส์กับคียร์บอร์ด
                'accid': 'รหัสสินค้า',
                'name': 'ชื่อสินค้า',
                'model': 'รุ่น',
                'brand': 'ยี่ห้อ',
                'color': 'สี',
                'keyswitch': 'รูปแบบสวิทซ์',
                'keypresslifetime': 'กดได้กี่ครั้ง',
                'numberkey': 'จำนวนปุ่ม',
                'mediakey': 'กดสูงสุดได้กี่ปุ่ม',
                'interface': 'interface',
                'size': 'ขนาด',
                'description': 'รายละเอียด',
                'image': 'รูปภาพ',
                'weight': 'น้ำหนัก',
                'price': 'ราคา',
                'net': 'คงเหลือ',
                'warranty': 'ประกัน',
                'category': 'ประเภทสินค้า',
        }
    def setForUpdate(self):
        self.fields['storageid'].widget.attrs['readonly'] = True
        self.fields['storageid'].widget.attrs['style'] = 'background-color: #f9f9f9;'
        self.fields['storageid'].label = 'รหัสสินค้า (ไม่สามารถแก้ไขได้)'
        
class StorageForm(forms.Modelform):
    class Meta:
        model = Storage
        fields = '__all__'
        widgest = {
            'storageid': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'RPM': forms.TextInput(attrs={'class': 'form-control'}),
            'Form_Factor': forms.TextInput(attrs={'class': 'form-control'}),
            'Random_Write': forms.TextInput(attrs={'class': 'form-control'}),
            'Random_Read': forms.TextInput(attrs={'class': 'form-control'}),
            'Sequential_Write': forms.TextInput(attrs={'class': 'form-control'}),
            'Sequential_Read': forms.TextInput(attrs={'class': 'form-control'}),
            'interface': forms.TextInput(attrs={'class': 'form-control', 'min': '1', 'step': '0.25'}),
            'technology': forms.TextInput(attrs={'class': 'form-control','min': '0'}),
            'size_ssd': forms.FileInput(attrs={'class': 'form-control'}),
            'storage' : forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'min': '1', 'step': '0.25'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'net': forms.TextInput(attrs={'class': 'form-control'}),
            'warranty': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labes = {
            # ssd กับ hdd
            'storageid': 'รหัสสินค้า',
            'name': 'ชื่อสินค้า',
            'model': 'รุ่น',
            'brand': 'ยี่ห้อ',
            'RPM': 'RPM',
            'Form_Factor': 'Form Factor',
            'Random_Write': 'การเขียนข้อมูล',
            'Random_Read': 'การอ่านข้อมูล',
            'Sequential_Write': 'ความเร็วสูงสุดในการเขียนข้อมูล',
            'Sequential_Read': 'ความเร็วสูงสุดในการอ่านข้อมูล',
            'interface': 'interface',
            'technology': 'Technology',
            'size_ssd': 'ขนาด SSD',
            'storage': 'หน่วยความจำ',
            'weight': 'น้ำหนัก',
            'price': 'ราคา',
            'description': 'รายละเอียด',
            'image': 'รูปภาพ',
            'net': 'คงเหลือ',
            'warranty': 'ประกัน',
            'category': 'ประเภทสินค้า',
        }
    def setForUpdate(self):
        self.fields['storageid'].widget.attrs['readonly'] = True
        self.fields['storageid'].widget.attrs['style'] = 'background-color: #f9f9f9;'
        self.fields['storageid'].label = 'รหัสสินค้า (ไม่สามารถแก้ไขได้)'

class NetworkForm(forms.Modelform):
    class Meta:
        model = NetworkDevice
        fields = '__all__'
        widgest = {
            'ntid': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'system_management': forms.TextInput(attrs={'class': 'form-control'}),
            'power_supply': forms.TextInput(attrs={'class': 'form-control'}),
            'optical_drive': forms.TextInput(attrs={'class': 'form-control'}),
            'raid_controller': forms.TextInput(attrs={'class': 'form-control'}),
            'harddisk': forms.TextInput(attrs={'class': 'form-control'}),
            'memory': forms.TextInput(attrs={'class': 'form-control'}),
            'processor_speed': forms.TextInput(attrs={'class': 'form-control'}),
            'processor': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'net': forms.TextInput(attrs={'class': 'form-control'}),
            'warranty': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labes = {
            #อุปกรณ์เครือข่าย
            'ntid': 'รหัสสินค้า',
            'name': 'ชื่อสินค้า',
            'model': 'รุ่น',
            'brand': 'ยี่ห้อ',
            'system_management': 'ระบบปฎิบัติการ',
            'power_supply': 'แหล่งจ่ายไฟ',
            'optical_drive': 'ไดรฟ์ออปติคัล',
            'raid_controller': 'ตัวควบคุม RAID',
            'harddisk': 'ฮาร์ดดิสก์',
            'memory': 'หน่วยความจำ',
            'processor_speed': 'ความเร็วของโปรเซสเซอร์',
            'processor': 'โปรเซสเซอร์',
            'weight': 'น้ำหนัก',
            'price': 'ราคา',
            'description': 'รายละเอียด',
            'image': 'รูปภาพ',
            'net': 'คงเหลือ',
            'warranty': 'ประกัน',
            'category': 'ประเภทสินค้า',
        }
    def setForUpdate(self):
        self.fields['ntid'].widget.attrs['readonly'] = True
        self.fields['ntid'].widget.attrs['style'] = 'background-color: #f9f9f9;'
        self.fields['ntid'].label = 'รหัสสินค้า (ไม่สามารถแก้ไขได้)'
        
