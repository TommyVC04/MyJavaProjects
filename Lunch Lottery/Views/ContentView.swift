//
//  ContentView.swift
//  Lunch Lottery
//
//  Created by TommyVC04 on 8/29/22.
//

import SwiftUI
import UserNotifications

struct ContentView: View {
    
    var body: some View {
        LandmarkList(profile: Profile.default)
    }
    
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .environmentObject(ModelData())
    }
}
