//
//  ScheduleView.swift
//  Lunch Lottery
//
//  Created by 2390004 on 10/12/22.
//

import SwiftUI

struct ScheduleView: View {
    @EnvironmentObject var modelData: ModelData

    var filteredLandmarks: [Landmark] {
        modelData.landmarks.filter { landmark in
            (landmark.isConfirmed)
        }
    }

    var body: some View {
        NavigationView {
            List {
                ForEach(filteredLandmarks) { landmark in
                    NavigationLink {
                        LandmarkDetail(landmark: landmark)
                    } label: {
                        LandmarkRow(landmark: landmark)
                    }
                }
            }
            .navigationTitle("Scheduled Lotteries")
        }
    }
}

struct ScheduleView_Previews: PreviewProvider {
    static var previews: some View {
        ScheduleView()
            .environmentObject(ModelData())
    }
}
