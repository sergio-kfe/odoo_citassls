# -*- coding: utf-8 -*-

from odoo import models,api,fields

class citassls(models.Model):
    _name='sls.citassls'

    autor = fields.Many2one('res.users', default = lambda self: self.env.user)
    cita = fields.Text(required=True)
    fecha = fields.Date(default=fields.Date.today)
    orden = fields.Integer()
    

    @api.onchange('fecha')
    def _onchange_fecha(self):
	cr=self.env.cr
	fecha=str(self.fecha)
	autor=int(self.autor)
	try:
        	cr.execute("SELECT max(orden) FROM sls_citassls AS a WHERE (CAST(a.fecha AS varchar(20)) LIKE '%s') and autor = %s" % (fecha, autor))
		cont=cr.fetchone()[0]
	except:
		cont=0

	if cont == None:	
		cont=0

	self.orden = cont+1;

    @api.onchange('autor')
    def _onchange_autor(self):
	cr=self.env.cr
	fecha=str(self.fecha)
	autor=int(self.autor)
	try:
        	cr.execute("SELECT max(orden) FROM sls_citassls AS a WHERE (CAST(a.fecha AS varchar(20)) LIKE '%s') and autor = %s" % (fecha, autor))
		cont=cr.fetchone()[0]
	except:
		cont=0

	if cont == None:	
		cont=0

	self.orden = cont+1;
    @api.one
    def eliminar(self):
	autor=int(self.autor)
	fecha=str(self.fecha)
	orden=int(self.orden)
	try:
        	 self.env.cr.execute("delete FROM sls_citassls AS a WHERE (CAST(a.fecha AS varchar(20)) LIKE '%s') and autor = %s and orden= %s" % (fecha, autor, orden))
	except:
		self.cita = "delete FROM sls_citassls AS a WHERE (CAST(a.fecha AS varchar(20)) LIKE '%s') and autor = %s and orden= %s" % (fecha, autor, orden);
