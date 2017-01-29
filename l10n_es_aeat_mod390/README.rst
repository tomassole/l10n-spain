.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

================================
Presentación del Modelo AEAT 390
================================

Modelo 390 de la AEAT. Declaración-resumen anual del Impuesto sobre el Valor
Añadido.

Instalación
===========

Este módulo requiere del módulo *account_tax_balance* que se encuentra en
https://github.com/OCA/account-financial-reporting.

Uso
===

Para crear un modelo, por ejemplo de un trimestre del año:

1. Ir a *Contabilidad > Declaraciones AEAT > Modelo 390*.
2. Pulsar en el botón "Crear"
3. Seleccionar el ejercicio fiscal.
4. Seleccionar el tipo de declaración.
5. Rellenar el teléfono y teléfono móvil, necesarios para la exportacion BOE
6. Guardar y pulsar en el botón "Calcular"
7. Rellenar (si es necesario) aquellos campos que Odoo no calcula
   automáticamente.
8. Cuando los valores sean los correctos, pulsar en el botón "Confirmar"
9. Podemos exportar en formato BOE para presentarlo telemáticamente en el
   portal de la AEAT

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Pruébalo en Runbot
   :target: https://runbot.odoo-community.org/runbot/189/9.0

Gestión de errores
==================

Los errores/fallos se gestionan en `las incidencias de GitHub <https://github.com/OCA/
l10n-spain/issues>`_.
En caso de problemas, compruebe por favor si su incidencia ha sido ya
reportada. Si fue el primero en descubrirla, ayúdenos a solucionarla indicando
una detallada descripción `aquí <https://github.com/OCA/l10n-spain/issues/new>`_.

Problemas conocidos / Hoja de ruta
==================================

* La declaración sólo se puede realizar para personas jurídicas.
* No se han implementado todas las casillas de opciones de la empresa, como
  por ejemplo si la empresa está en concurso de acreedores o si pertenece
  al registro de devolución mensual.
* No se calculan operaciones intragrupo.
* No se contempla el régimen de criterio de caja.
* No se contempla el régimen especial de bienes usados, objetos de arte,
  antigüedades y objetos de colección.
* No se contempla el régimen especial de agencias de viaje.
* No se contempla el régimen especial de la agricultura, ganadería y pesca.
* No se contempla la prorrata general de IVA.
* No se contempla el régimen simplificado.
* No se contempla el régimen de deducción diferenciado.
* No se contempla la inversión de sujeto pasivo nacional.
* No se ha incluido el cálculo para los bienes de inversión.
* No se ha incluido el cálculo para otros supuestos de inversión de sujeto
  pasivo.
* No se tienen en cuenta tributaciones territoriales.
* Obtener las casillas 95, 97 y 98 de las declaraciones del 303.

Créditos
========

Contribuidores
--------------

* Pedro M. Baeza <pedro.baeza@tecnativa.com>

Financiadores
-------------

La migración de este módulo forma parte de una campaña de migración de la
localización española que ha sido posible gracias a la colaboración económica
de las siguientes empresas (por orden alfabético):

* `Aizean evolution <http://www.aizean.com>`_
* `Aselcis consulting <https://www.aselcis.com>`_
* `AvanzOSC <http://avanzosc.es>`_
* `Diagram software <http://diagram.es>`_
* `Domatix <http://www.domatix.com>`_
* `Eficent <http://www.eficent.com>`_
* `FactorLibre <http://factorlibre.com>`_
* `Fairhall solutions <http://www.fairhall.es>`_
* `GAFIC SLP <http://www.gafic.com>`_
* `Incaser <http://www.incaser.es>`_
* `Ingeos <http://www.ingeos.es>`_
* `Nubistalia <http://www.nubistalia.es>`_
* `Punt sistemes <http://www.puntsistemes.es>`_
* `Praxya <http://praxya.com>`_
* `Reeng <http://www.reng.es>`_
* `Soluntec <http://www.soluntec.es>`_
* `Tecnativa <https://www.tecnativa.com>`_
* `Trey <https://www.trey.es>`_
* `Vicent Cubells <http://vcubells.net>`_

Maintainer
----------

.. image:: http://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: http://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit http://odoo-community.org.
