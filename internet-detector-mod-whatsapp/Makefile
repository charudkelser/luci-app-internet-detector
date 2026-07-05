include $(TOPDIR)/rules.mk

PKG_NAME:=internet-detector-mod-whatsapp
PKG_VERSION:=1.0.0
PKG_RELEASE:=1

include $(INCLUDE_DIR)/package.mk

define Package/internet-detector-mod-whatsapp
  SECTION:=net
  CATEGORY:=Network
  TITLE:=WhatsApp notification module for internet-detector
  PKGARCH:=all
  DEPENDS:=+internet-detector +curl
endef

define Package/internet-detector-mod-whatsapp/install
	$(INSTALL_DIR) $(1)/usr/lib/lua/internet-detector/modules
	$(INSTALL_DATA) ./data/usr/lib/lua/internet-detector/modules/mod_whatsapp.lua $(1)/usr/lib/lua/internet-detector/modules/
	
	$(INSTALL_DIR) $(1)/usr/share/rpcd/acl.d
	$(INSTALL_DATA) ./luci/usr/share/rpcd/acl.d/luci-app-internet-detector-mod-whatsapp.json $(1)/usr/share/rpcd/acl.d/
	
	$(INSTALL_DIR) $(1)/usr/share/rpcd/ucode
	$(INSTALL_DATA) ./luci/usr/share/rpcd/ucode/luci.internet-detector-mod-whatsapp $(1)/usr/share/rpcd/ucode/
endef

$(eval $(call BuildPackage,internet-detector-mod-whatsapp))
