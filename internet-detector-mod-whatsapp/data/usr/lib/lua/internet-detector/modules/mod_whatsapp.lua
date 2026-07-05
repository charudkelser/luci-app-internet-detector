--[[
	Dependences:
		curl
--]]
local unistd = require("posix.unistd")

local Module = {
	name                 = "mod_whatsapp",
	runPrio              = 70,
	syslog               = function(level, msg) return true end,
	debugOutput          = function(msg) return true end,
	waApiKey             = nil,
	waPhoneNumber        = nil,
	waMsgURLpattern      = "https://api.callmebot.com/whatsapp.php?phone=%s&text=%s&apikey=%s",
	msgTextPattern       = "[%s] (%s) @ %s",
}

function Module:init(t)
	self._enabled = true
	if t.api_key then self.waApiKey = t.api_key end
	if t.phone_number then self.waPhoneNumber = t.phone_number end
	if not self.waApiKey or not self.waPhoneNumber then
		self._enabled = false
		self.syslog("err", "WhatsApp API key or Phone Number not specified.")
	end
end

function Module:messageRequest(msg, textPattern)
	local waMsg = string.format(textPattern, self.hostAlias, self.config.serviceConfig.instance, msg)
	local url   = string.format(self.waMsgURLpattern, self.waPhoneNumber, self:escape(waMsg), self.waApiKey)
	local retCode, data = self:httpRequest(url)
	return retCode
end
