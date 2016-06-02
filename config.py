# -*- coding: utf-8 -*-
import ConfigParser

class Config:
    def readConfig(self, file):
        conf = ConfigParser.SafeConfigParser()
        conf.read(file)
        self.output_dir               = conf.get('filepath', 'output_dir')
        self.gui_setting_file         = conf.get('filepath', 'gui_setting_file')
        self.network_file             = conf.get('filepath', 'network_file')
        self.route_file               = conf.get('filepath', 'route_file')
        self.vehicle_file             = conf.get('filepath', 'vehicle_file')
        self.parkinglot_file          = conf.get('filepath', 'parkinglot_file')
        self.short_cut_file           = conf.get('filepath', 'short_cut_file')

        self.port                     = int(conf.get('options', 'port'))
        self.real_net                 = eval(conf.get('options', 'real_net'))
        self.parking                  = eval(conf.get('options', 'parking'))
        self.reroute                  = eval(conf.get('options', 'reroute'))
        self.negotiation              = eval(conf.get('options', 'negotiation'))
        self.iteration                = int(conf.get('options', 'iteration'))
        self.dce                      = eval(conf.get('options', 'dce'))
        self.dce_area                 = int(conf.get('options', 'dce_area'))
        self.redis_use                = eval(conf.get('options', 'redis_use'))
        self.redis_host               = str(conf.get('options', 'redis_host'))
        self.long_term_sd             = float(conf.get('options', 'long_term_sd'))
        self.short_term_sec           = int(conf.get('options', 'short_term_sec'))
        self.weight_of_past_stigmergy = float(conf.get('options', 'weight_of_past_stigmergy'))
        self.short_cut                = int(conf.get('options', 'short_cut'))
        self.alpha                    = float(conf.get('options', 'alpha'))
        self.beta                     = float(conf.get('options', 'beta'))
        self.congestion_bpr           = float(conf.get('options', 'congestion_bpr'))
        self.congestion_division      = float(conf.get('options', 'congestion_division'))
        self.congestion_judgement     = float(conf.get('options', 'congestion_judgement'))
        self.requesterB               = float(conf.get('options', 'requesterB'))
        self.requestedB               = float(conf.get('options', 'requestedB'))
        self.point                    = float(conf.get('options', 'point'))