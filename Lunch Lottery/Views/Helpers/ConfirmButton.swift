//
//  FavoriteButton.swift
//  Lunch Lottery
//
//  Created by TommyVC04 on 9/7/22.
//

import SwiftUI

struct ConfirmButton: View {
    @Binding var isSet: Bool
    @State private var showSure = false
    @EnvironmentObject var modelData: ModelData
    var landmarkIndex: Int

    var body: some View {
        Button (action: {showSure = true} ){
            Text("Confirm")
        }
        .padding()
        .foregroundColor(.white)
        .background(Color.blue)
        .clipShape(RoundedRectangle(cornerRadius: 5))
        .confirmationDialog("Are you sure?", isPresented: $showSure, titleVisibility: .visible) {
            Button("Yes", role: .destructive) {
                isSet.toggle()
                modelData.landmarks[landmarkIndex].isConfirmed = isSet
            }
            Button("Cancel", role: .cancel) {}
        }
    }
}

func confirm() {
    //ENTER LOTTERY
}

struct ConfirmButton_Previews: PreviewProvider {
    static var previews: some View {
        ConfirmButton(isSet: .constant(false), landmarkIndex: 0)
            .environmentObject(ModelData())
    }
}
