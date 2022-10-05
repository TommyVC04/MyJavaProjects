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
        NavigationView {
            if (chosenOrg) {
                schoolView
            }
            else {
                noOrgView
            }
        }
    }
    
    var noOrgView: some View {
        NavigationView {
            List {
                Text("Edit Profile to Select School")
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
    /*
    func checkSchool () {
        chosenOrg = modelData.profile.school.rawValue != "Choose a School / Organization"
    }
     
     ForEach(modelData.categories.keys.sorted(), id: \.self) { key in
         CategoryRow(categoryName: key, items: modelData.categories[key]!)
     }
     */
    
    var schoolView: some View {
        NavigationView {
            List {
                //let strKey = 
                ForEach((modelData.categories[profile.school.rawValue] ?? modelData.categories["Test"])!) { landmark in
                    NavigationLink {
                        LandmarkDetail(landmark: landmark)
                    } label: {
                        LandmarkRow(landmark: landmark)
                    }
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
