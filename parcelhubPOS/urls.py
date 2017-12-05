from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout
from django.conf.urls import handler404, handler500
urlpatterns = [
    url(r'^$', views.loginuser, name='login'),          
    url(r'^logout/$', logout, {'next_page': '/parcelhubPOS/'}, name='logout'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^masterdata/$', views.masterdata, name='masterdata'),
    url(r'^invoice/$', views.invoice, name='invoice'),
    url(r'^invoice/editinvoice(?P<invoiceid>\w{0,50})/$', views.editInvoice, name='editinvoice'),
    url(r'^invoice/deleteinvoice(?P<dinvoiceid>\w{0,50})/$', views.deleteinvoice, name='deleteinvoice'),
    url(r'^autocompletesku/$',views.autocompletesku, name='autocompletesku'),
    url(r'^autocompleteskufield/$',views.autocompleteskufield, name='autocompleteskufield'),
    url(r'^autocompleteskudetail/$',views.autocompleteskudetail, name='autocompleteskudetail'),
    url(r'^autocompletezone/$',views.autocompletezone, name='autocompletezone'),
    url(r'^validatetrackingcode/$',views.validatetrackingcode, name='validatetrackingcode'),
    url(r'^validateweightrange/$',views.validateweightrange, name='validateweightrange'),
    url(r'^autocompleteweight/$',views.autocompleteweight, name='autocompleteweight'),
    url(r'^hideshowcustomer/$',views.hideshowcustomer, name='hideshowcustomer'),
    url(r'^sku/$', views.SKUlist, name='sku'),
    url(r'^sku/editsku(?P<skucode>\w{0,50})/$', views.editSKU, name='editsku'),
    url(r'^sku/deletesku(?P<dskucode>\w{0,50})/$', views.deleteSKU, name='deletesku'),
    url(r'^branch/$', views.branchlist, name='branchlist'),
    url(r'^branch/editbranch(?P<ebranchid>\w{0,50})/$', views.editbranch, name='editbranch'),
    url(r'^branch/deletebranch(?P<dbranchid>\w{0,50})/$', views.deletebranch, name='deletebranch'),
    url(r'^vendor/$', views.vendorlist, name='vendor'),
    url(r'^vendor/editvendor(?P<vendorid>\w{0,50})/$', views.editvendor, name='editvendor'),
    url(r'^vendor/deletevendor(?P<dvendorid>\w{0,50})/$', views.deletevendor, name='deletevendor'),
    url(r'^zonedomestic/$', views.zonedomesticlist, name='zonedomestic'),
    url(r'^zonedomestic/editzonedomestic(?P<zonedomesticid>\w{0,50})/$', views.editzonedomestic, name='editzonedomestic'),
    url(r'^zonedomestic/deletezonedomestic(?P<dzonedomesticid>\w{0,50})/$', views.deletezonedomestic, name='deletezonedomestic'),
    url(r'^zoneinternational/$', views.zoneinternationallist, name='zoneinternational'),
    url(r'^zoneinternational/editzoneinternational(?P<zoneinternationalid>\w{0,50})/$', views.editzoneinternational, name='editzoneinternational'),
    url(r'^zoneinternational/deletezoneinternational(?P<dzoneinternationalid>\w{0,50})/$', views.deletezoneinternational, name='deletezoneinternational'),
    url(r'^tax/$', views.taxlist, name='tax'),
    url(r'^tax/edittax(?P<taxid>\w{0,50})/$', views.edittax, name='edittax'),
    url(r'^tax/deletetax(?P<dtaxid>\w{0,50})/$', views.deletetax, name='deletetax'),
    url(r'^user/$', views.userlist, name='user'),
    url(r'^user/adduser/$', views.adduser, name='adduser'),
    url(r'^user/edituser(?P<user_id>\w{0,50})/$', views.edituser, name='edituser'),
    url(r'^user/deleteuser(?P<duser_id>\w{0,50})/$', views.deleteuser, name='deleteuser'),
    url(r'^user/password(?P<user_id>\w{0,50})/$', views.change_password, name='change_password'),
    url(r'^user/userbranchaccess(?P<user_id>\w{0,50})/$', views.userbranchaccess, name='userbranchaccess'),
    url(r'^user/userbranchaccess/edituba(?P<userbranch_id>\w{0,50})/$', views.edituserbranchaccess, name='edituserbranchaccess'),
    url(r'^user/userbranchaccess/deleteuba(?P<duserbranch_id>\w{0,50})/$', views.deleteuserbranchaccess, name='deleteuserbranchaccess'),
    url(r'^skubranch/$', views.skubranchlist, name='skubranch'),
    url(r'^skubranch/editskubranch(?P<skubranchid>\w{0,50})/$', views.editskubranch, name='editskubranch'),
    url(r'^skubranch/deleteskubranch(?P<dskubranchid>\w{0,50})/$', views.deleteskubranch, name='deleteskubranch'),
    url(r'^customer/$', views.customerlist, name='customer'),
    url(r'^statementofaccount/$', views.statementofacclist, name='statementofaccount'),
    url(r'^statementofaccount/viewsoa/$', views.viewstatementofacc, name='viewstatementofacc'),
    url(r'^statementofaccount/deletesoa(?P<dsoaid>\w{0,50})/$$', views.deletestatementofacc, name='deletestatementofacc'),
    url(r'^payment(?P<custid>\w{0,50})/$', views.paymentlist, name='payment'),
    url(r'^payment/editpayment(?P<paymentid>\w{0,50})/$', views.editpayment, name='editpayment'),
    url(r'^payment/deletepayment(?P<dpaymentid>\w{0,50})/$$', views.deletepayment, name='deletepayment'),
    #url(r'^customer/customerdocuments(?P<customer_id>\w{0,50})/$', views.customerdocuments, name='customerdocuments'),
    url(r'^customer/editcustomer(?P<customerid>\w{0,50})/$', views.editcustomer, name='editcustomer'),
    url(r'^customer/deletecustomer(?P<dcustomerid>\w{0,50})/$', views.deletecustomer, name='deletecustomer'),
]
