//
//  Lunch_LotteryApp.swift
//  Lunch Lottery
//
//  Created by TommyVC04 on 8/29/22.
//

import SwiftUI

@main
struct Lunch_LotteryApp: App {
    @State private var modelData = ModelData()
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(modelData)
        }
    }
}
