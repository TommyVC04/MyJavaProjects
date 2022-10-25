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
        let chosenOrg = modelData.profile.school.rawValue != "Choose a School / Organization"
        if (chosenOrg) {
            schoolView
        }
        else {
            noOrgView
        }
    }
    
    var noOrgView: some View {
        NavigationView {
            List {
                Text("Edit Profile to Select School")
            }
            .listStyle(.automatic)
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
    
    var schoolView: some View {
        NavigationView {
            List {
                let strKey = modelData.profile.school.rawValue
                ForEach((modelData.categories[strKey] ?? modelData.categories["Test"])!) { landmark in
                    NavigationLink {
                        LandmarkDetail(landmark: landmark)
                    } label: {
                        LandmarkRow(landmark: landmark)
                    }
                }
            }
            .listStyle(.automatic)
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
