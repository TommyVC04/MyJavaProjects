//
//  LandmarkList.swift
//  Lunch Lottery
//
//  Created by TommyVC04 on 9/2/22.
//

import SwiftUI

struct LandmarkList: View {
    @EnvironmentObject var modelData: ModelData
    @State private var showingProfile = false
    var profile: Profile
    
    var body: some View {
        NavigationView {
            List {
                
                if (profile.school.rawValue != "Choose a School / Organizaiton") {
                
                ForEach(modelData.landmarks) { landmark in
                    NavigationLink {
                        LandmarkDetail(landmark: landmark)
                    } label: {
                        LandmarkRow(landmark: landmark)
                    }
                }
                
                }
                else {
                    Text("Edit Profile to Select School")
                }
                
            }
            .navigationTitle("Lunch Lotteries")
            .toolbar {
                Button {
                    showingProfile.toggle()
                } label: {
                    Label("User Profile", systemImage: "person.crop.circle")
                }
            }
            .sheet(isPresented: $showingProfile) {
                ProfileHost()
                    .environmentObject(modelData)
            }
        }
    }
}

struct LandmarkList_Previews: PreviewProvider {
    static var previews: some View {
        LandmarkList(profile: Profile.default)
            .environmentObject(ModelData())
    }
}
