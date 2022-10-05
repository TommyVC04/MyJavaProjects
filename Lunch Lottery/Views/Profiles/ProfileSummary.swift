//
//  ProfileSummary.swift
//  Lunch Lottery
//
//  Created by TommyVC04 on 9/14/22.
//

import SwiftUI

struct ProfileSummary: View {
    @EnvironmentObject var modelData: ModelData
    var profile: Profile

    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 10) {
                Text("Name: \(profile.username == "" ? "~": profile.username)")
                    .bold()
                    .font(.title)

                Text("Notifications: \(profile.prefersNotifications ? "On": "Off" )")
                Text("School / Organization: \(profile.school.rawValue == "Choose a School / Organization" ? "~": profile.school.rawValue)")
                
                Divider()
                
                VStack(alignment: .leading) {
                    Text("Scheduled Lotteries")
                        .font(.headline)

                    HikeView(hike: modelData.hikes[0])
                }
            }
        }
    }
}

struct ProfileSummary_Previews: PreviewProvider {
    static var previews: some View {
        ProfileSummary(profile: Profile.default)
            .environmentObject(ModelData())
    }
}
